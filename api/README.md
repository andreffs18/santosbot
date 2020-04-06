# Backend API

Very simple HTTP webserver build with on Python 3.7, using Starlette, an ASGI Framework.


## Install 

You can either use a virtual env and setup the project locally with poetry install or use docker



To install this you need:

```shell
$ git clone
$ mkvirtualenv santosbot
$ pip install -r requirements.txt
```


```
$ docker build -t santosbot:latest .

$ docker run --rm -it -p 1234:8000 --env-file .env -v $(PWD):/app/ santosbot-api /bin/bash

## Usage

This api simple exposes two endpoints
/ version 
/ bot

Bot GET requests


### Make it talk!
To see it working, you just need to invite him to a slack channel and start talking. 
Whever a **Trigger Word** is typed, he will select a random quote and post it as a reply to whatever you were saying.

> You can find all Trigger Words on [/utils/quotes.py:123](https://github.com/andreffs18/santosbot/blob/master/utils/quotes.py#L188)


![](https://i.imgur.com/56XcpeI.png)



