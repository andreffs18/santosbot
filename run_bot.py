# -*- coding: utf-8 -*-
import os
import time
import random
from datetime import datetime, timedelta

from slackclient import SlackClient

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME", 'santosbot')
BOT_ID = os.environ.get("BOT_ID")
# 1 second delay between reading from firehose
READ_WEBSOCKET_DELAY = 1
# timeout before re-using the same quote
QUOTE_REUSE_TIMEOUT = 15 # seconds

QUOTES = {
	0: u"O único preço da tua liberdade é a responsabilidade que tens por escolheres usá-la.",
	1: u"Assim como os confiantes atraem os confiantes, os invejosos, rancorosos e maldosos também se atraem uns aos outros.",
	2: u"Quem pensa por si, afirma o que sente e materializa as suas vontades, será sempre controverso, mas é precisamente da controvérsia que nasce a mudança, é do desacordo que se dá a evolução da alma.",
	3: u"A liberdade é o expoente máximo do amor-próprio.",
	4: u"Só aquele que ousa, por sua livre e espontânea vontade, abandonar o rebanho da indolência para fazer o seu próprio destino é que alcançará, verdadeiramente, o total poder da alma que é.",
	5: u"Não te queixes da vida, não fiques à espera dela, cria-a, e terás a vida que sempre sonhaste.",
	6: u"Uma pessoa que não sonha não encontra motivos, realmente fortes, para acordar todas as manhãs com vontade de viver, nãqo se conecta com a divindade em si mesma.",
}

TRIGGER_WORDS = {
	u'liberdade': {'quotes': [0, 3], 'last_used_at': datetime.min},
	u'responsabilidade': {'quotes': [0], 'last_used_at': datetime.min},
	u'escolher': {'quotes': [0], 'last_used_at': datetime.min},
	u'escolhas': {'quotes': [0], 'last_used_at': datetime.min},
	u'escolha': {'quotes': [0], 'last_used_at': datetime.min},
	u'confiança': {'quotes': [1], 'last_used_at': datetime.min},
	u'confiante': {'quotes': [1], 'last_used_at': datetime.min},
	u'atração': {'quotes': [1], 'last_used_at': datetime.min},
	u'atrair': {'quotes': [1], 'last_used_at': datetime.min},
	u'invejosa': {'quotes': [1], 'last_used_at': datetime.min},
	u'invejoso': {'quotes': [1], 'last_used_at': datetime.min},
	u'sentimos': {'quotes': [2], 'last_used_at': datetime.min},
	u'sentimentos': {'quotes': [2], 'last_used_at': datetime.min},
	u'amor': {'quotes': [3], 'last_used_at': datetime.min},
}


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


def parse_slack_output(slack_rtm_output):
	"""The Slack Real Time Messaging API is an events firehose. 
	This parsing function returns None unless a message is directed
	at the Bot, based on its ID.
	"""
	output_list = slack_rtm_output
	if output_list and len(output_list) > 0:
		print(datetime.now(), output_list)
		for output in output_list:
			if output.get('type') != 'message':
				continue

			print(datetime.now(), output_list)
			
			text = output.get('text', "")
			tokenized_text = filter(None, map(lambda x: x.strip().lower(), text.split()))
			intersection = set(TRIGGER_WORDS).intersection(tokenized_text)
			
			if intersection:
				word = random.choice(list(intersection))
				quote_id = random.choice(TRIGGER_WORDS.get(word).get('quotes'))
				quote = QUOTES.get(quote_id)
				last_used_at = TRIGGER_WORDS.get(word).get('last_used_at')
				if last_used_at + timedelta(seconds=QUOTE_REUSE_TIMEOUT) > datetime.now():
					print(u"Skipping quote for \"{}\", last used {} and it will be available {}s after.".format(word, last_used_at, QUOTE_REUSE_TIMEOUT))
					continue

				trigger_word = TRIGGER_WORDS.get(word)
				trigger_word.update({'last_used_at': datetime.now()})

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
			parse_slack_output(slack_client.rtm_read())
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print("Connection failed. Invalid Slack token or bot ID?")
