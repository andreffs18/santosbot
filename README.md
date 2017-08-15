# Santosbot

SlackBot that spits out quotes from Gustavo Santos whenever a **Trigger Word** is written.

![](https://i.imgur.com/nM3mJd3.jpg)


## Install 

To install this you need:

```shell
$ git clone
$ mkvirtualenv santosbot
[santosbot] $ pip install -r requirements.txt
```

## Setup Bot

This project runs entirely on the [SlackClient](https://github.com/slackapi/python-slackclient) for python by taking advantage of the [**RTM Api**](https://api.slack.com/rtm).

### Create Bot
First of all you need to create a new Bot. For the sake of the joke, we will call it **santosbot**. You just need to go to "https://api.slack.com/bot-users" under "Custom bot users", and submit your bot name.

![](https://i.imgur.com/TSYs9Tc.png)

Once you have your new bot created, you need to save the **API Token** that is under **Integration Settings** section.
> You can customize your bot with a picture, first name and last name. For this project, we will be calling it **Gugu Santos**

### Running "SantosBot" Server

Now, that we already have our API token, we just need to run the project like so:
```shell
$ SLACK_BOT_TOKEN=xoxb-***** python run_bot.py
Got BOT_ID=<@U6BR114N7> for "santosbot"
"santosbot" connected and running!
(datetime.datetime(2017, 8, 15, 18, 14, 10, 302603), [{u'type': u'hello'}])
(datetime.datetime(2017, 8, 15, 18, 14, 11, 303554), [{u'url': u'**', u'type': u'reconnect_url'}])
(...)
```

### Make it talk!
To see it working, you just need to invite him to a slack channel and start talking. 
Whever a **Trigger Word** is typed, he will select a random quote and post it as a reply to whatever you were saying.

> You can find all Trigger Words on [/utils/quotes.py:123](https://github.com/andreffs18/santosbot/blob/master/utils/quotes.py#L188)


![](https://i.imgur.com/56XcpeI.png)



