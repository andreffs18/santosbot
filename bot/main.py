import os
import sys
import time
import logging
import requests
from requests.exceptions import ConnectionError
from slackclient import SlackClient

# Backend API url
API_URL = os.environ.get("API_URL", "http://api:8888")
# Slack Bot Token: "https://api.slack.com/bot-users" under "Custom bot users"
SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
SLACK_BOT_NAME = os.environ.get("SLACK_BOT_NAME", "santosbot")
# 1 second delay between reading from firehose
READ_WEBSOCKET_DELAY = int(os.environ.get("READ_WEBSOCKET_DELAY", "1"))

# python slack client
slack_client = SlackClient(SLACK_API_TOKEN)


def setup_logger():
	# create logger with 'spam_application'
	logger = logging.getLogger("bot")
	logger.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(ch)
	return logger


def cache_slack_users():
	"""Get list of users from slack and store key-value that keeps id->username"""
	response = slack_client.api_call("users.list", token=SLACK_API_TOKEN)
	if not response.get("ok"):
		return

	members = response.get('members')
	return dict(map(lambda u: (u.get('id'), u.get('name')), members))


def get_bot_id(users):
	"""From env BOT_NAME, call Slack Api and search for BOT_NAME's slack id"""
	user2id = dict([(name, id) for id, name in users.items()])
	return f"<@{user2id.get(SLACK_BOT_NAME)}>"


def parse_slack_output(users, slack_rtm_output):
	"""The Slack Real Time Messaging API is an events firehose. 
	This parsing function returns None unless a message is directed at the Bot, based on its ID."""
	output_list = slack_rtm_output
	if not output_list or len(output_list) == 0:
		return

	for output in output_list:
		if output.get('type') != 'message':
			continue

		logger.info(f'"{users.get(output.get("user"))}": "{output.get("text")}"')
		try:
			response = requests.get(API_URL + "/bot?text=" + output.get('text', ""))
			if not response.ok:
				continue
		except ConnectionError as e:
			logger.error(f'⚠️  {str(e)}')
			continue

		quote = response.json()["quote"]
		slack_client.api_call("chat.postMessage", channel=output['channel'], text=quote, as_user=True)


if __name__ == "__main__":
	logger = setup_logger()
	users = cache_slack_users()
	if not users:
		logger.error(f"Could not connect to Slack. Maybe SLACK_API_TOKEN was not properly configured.")
		sys.exit(1)

	# Get bot name UID
	bot_id = get_bot_id(users)
	if not bot_id:
		logger.error(f"No bot found! Closing!")
		sys.exit(1)
	logger.info(f"Found BOT_ID={bot_id}")

	# Try to start connection, exit if fails
	if not slack_client.rtm_connect():
		logger.info("Connection failed. Invalid Slack token or bot ID?")
		sys.exit(1)

	logger.info("\"{}\" connected and running!".format(SLACK_BOT_NAME))
	while True:
		parse_slack_output(users, slack_client.rtm_read())
		time.sleep(READ_WEBSOCKET_DELAY)


