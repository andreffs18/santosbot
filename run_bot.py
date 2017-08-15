# -*- coding: utf-8 -*-

# Configs
import os
import re
import time
import random
import string

from datetime import datetime, timedelta
from slackclient import SlackClient

from utils.quotes import QUOTES, TRIGGER_WORDS

# Slack Bot Token: "https://api.slack.com/bot-users" under "Custom bot users"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME", 'santosbot')
BOT_ID = os.environ.get("BOT_ID")

# 1 second delay between reading from firehose
READ_WEBSOCKET_DELAY = 1
# timeout before re-using the same quote
QUOTE_REUSE_TIMEOUT = 15 # seconds
# global variable to prevent double posting 
LAST_POST_AT = datetime.min
# python slack client 
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def get_bot_id():
	"""From env BOT_NAME, call Slack Api and search for BOT_NAME's slack id"""
	bot_string = "<@{}>"
	if BOT_ID:
		return bot_string.format(BOT_ID)

	response = slack_client.api_call("users.list", token=SLACK_BOT_TOKEN)
	members = response.get('members')
	members = map(lambda u: (u.get('name'), u.get('id')), members)
	return bot_string.format(dict(members).get(BOT_NAME))


def tokenize_string(text):
	"""Given a string "text" tokenize it and make it lower case so it's 
	easier to search for trigger words"""
	new_tokens = list()
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	text = regex.sub('', text)
	tokens = [t.strip().lower() for t in text.split()]
	return filter(None, tokens)
	

def parse_slack_output(slack_rtm_output):
	"""The Slack Real Time Messaging API is an events firehose. 
	This parsing function returns None unless a message is directed
	at the Bot, based on its ID."""
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		
		print(datetime.now(), output_list)
		
		for output in output_list:
			if output.get('type') != 'message':
				continue

			print(datetime.now(), output_list)	
			tokenized_text = tokenize_string(output.get('text', ""))
			intersection = set(TRIGGER_WORDS).intersection(tokenized_text)
			
			if intersection:
				word = random.choice(list(intersection))
				quote_id = random.choice(TRIGGER_WORDS.get(word).get('quotes'))
				quote = QUOTES.get(quote_id)
				last_used_at = TRIGGER_WORDS.get(word).get('last_used_at')
				if last_used_at + timedelta(seconds=QUOTE_REUSE_TIMEOUT) > datetime.now() :
					print(u"Skipping quote for \"{}\", last used {} and it will be available {}s after.".format(word, last_used_at, QUOTE_REUSE_TIMEOUT))
					continue

				trigger_word = TRIGGER_WORDS.get(word)
				trigger_word.update({'last_used_at': datetime.now()})
				LAST_POST_AT = datetime.now() 
				print(u"> FOUND QUOTE: {} = {}: {}".format(word, quote_id, quote))
				slack_client.api_call("chat.postMessage", channel=output['channel'], text=quote, as_user=True)


if __name__ == "__main__":
	# Get bot name UID
	AT_BOT = get_bot_id()
	print("Got BOT_ID={} for \"{}\"".format(AT_BOT, BOT_NAME))
	
	# Start connection
	if slack_client.rtm_connect():
		print("\"{}\" connected and running!".format(BOT_NAME))
		while True:
			if LAST_POST_AT + timedelta(seconds=QUOTE_REUSE_TIMEOUT) > datetime.now():
				print("Preventing double posting: last post @ {}".format(LAST_POST_AT))
				time.sleep(QUOTE_REUSE_TIMEOUT)
			parse_slack_output(slack_client.rtm_read())
			time.sleep(READ_WEBSOCKET_DELAY)			

	else:
		print("Connection failed. Invalid Slack token or bot ID?")
