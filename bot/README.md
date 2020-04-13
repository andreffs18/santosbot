# Slack Bot

SlackBot that spits out quotes from Gustavo Santos whenever a **Trigger Word** is written.

It runs entirely on the [SlackClient](https://github.com/slackapi/python-slackclient) for python by using the [**Real Time Messaging Api**](https://api.slack.com/rtm).

## Install 

To run you must install [docker](https://docs.docker.com/get-docker/) and run the following:

```shell script
# Build and run project
~/santosbot/bot $ docker build -t bot:latest .
~/santosbot/bot $ docker run --rm -it -v $(PWD):/app -e SLACK_API_TOKEN=$SLACK_API_TOKEN bot:latest 
```


## Usage
First of all you need to create a new Bot on your slack team. For the sake of the joke, we will call it **"santosbot"**. 
You just need to go to "https://api.slack.com/bot-users" under "Custom bot users", and submit your bot name.

![](https://i.imgur.com/TSYs9Tc.png)

Once you have your new bot created, you need to save the **API Token** that is under **Integration Settings** section.
> You can customize your bot with a picture, first name and last name. For this project, we will be calling it **Gustavo Santos**


Now that we already have our API token, we just need to set the environment variable: 
```shell script
~/santosbot/bot $ export SLACK_API_TOKEN=xoxb-*****
~/santosbot/bot $ docker run --rm -it -v $(PWD):/app -e SLACK_API_TOKEN=$SLACK_API_TOKEN bot:latest
2020-04-10 16:01:52,999 - bot - INFO - Found BOT_ID=<@U6BR114N7>
2020-04-10 16:01:53,860 - bot - INFO - "santosbot" connected and running!
2020-04-10 16:02:03,893 - bot - INFO - "andreffs18": "Ola mundo"
2020-04-10 16:02:06,730 - bot - INFO - "santosbot": "É o amor, ou a falta dele, que rege o mundo. Nada de bom acontece na sua ausência e todos os passos que possam ser dados sem o seu cunho serão passos em falso."
(...)
```


![](https://i.imgur.com/56XcpeI.png)


### Environment Variables

The only variable that we need to setup to make this bot work is the `SLACK_API_TOKEN`. The remaining have already default values. Below is the description of each:

| Variable | Description | Default value | 
| ----- | ----- | ----- | 
| `API_URL` | Url for requesting quotes on backend service. Default value is set to communicate with the docker container when we use `docker-compose up` | "http://api:8888" | 
| `SLACK_BOT_NAME` | Bot name. This variable is configured when we setup the slack bot. | "santosbot" | 
| `SLACK_API_TOKEN` | Slack token that allows us to crawl messages from a particular channel. | Not defined. | 
| `READ_WEBSOCKET_DELAY` | Time spent, in seconds, waiting for the next message fetch. | "1" |
  
So, instead of defining every variable on the `$ docker run` command, we can do something like:

```shell script
~/santosbot/bot $ cat <<EOT >> .env
API_URL=http://localhost:8888
SLACK_BOT_NAME=santosbot
SLACK_API_TOKEN=$SLACK_API_TOKEN
READ_WEBSOCKET_DELAY=0
EOT
~/santosbot/bot $ docker run --rm -it -v $(PWD):/app --env-file .env bot:latest
2020-04-10 16:01:52,999 - bot - INFO - Found BOT_ID=<@U6BR114N7>
2020-04-10 16:01:53,860 - bot - INFO - "santosbot" connected and running!
2020-04-10 16:02:03,893 - bot - INFO - "andreffs18": "Ola mundo"
(...)
```