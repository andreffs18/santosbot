<h1 align="center">
  <a href="#">
    <img src="https://i.imgur.com/nM3mJd3.jpg" width="400">
  </a>
  <br><br>
</h1>

<h4 align="center">
    Slack Bot that spits out quotes from Gustavo Santos whenever a *<a href="https://santosbot.herokuapp.com/api/words" target="_blank" >Trigger Word</a>* is written.
</h4>

<p align="center">  
  <a href="https://github.com/andreffs18/santosbot/blob/master/LICENSE.md">
    <img src="https://img.shields.io/github/license/andreffs18/santosbot?color=yellow&style=flat-square" />
  </a>
  <a href="https://twitter.com/andreffs18">
    <img src="https://img.shields.io/badge/twitter-%40andreffs18-00ACEE.svg?style=flat-square" />
  </a>
</p>

<div align="center">
  <h4>
    <a href="#installation">Installation</a> |
    <a href="#usage">Usage</a> | 
    <a href="#deployment">Deployment</a>
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by <a href="https://andreffs.com">André Silva</a></sub>
</div>
<br>



## Installation

To run this locally you just need to have [docker](https://docs.docker.com/get-docker/) installed.  

<p align="center"><img src="/terminalizer.gif?raw=true"/></p>

Make sure you export your `SLACK_API_TOKEN`. More on that can be found on the [/bot](/bot/README.md) README file.

```shell script
$ export SLACK_API_TOKEN=xoxb-*****
```

## Usage

This project is divided into 3 parts:

- [Backend API](/backend/README.md): Python ASGI web server that exposes an web API for getting quotes.
- [Frontend App](/frontend/README.md): VueJS app that helps to showcase bot functionality.
- [Slack Bot](/bot/README.md): Actual slack bot that you can run to interact with.

By running with `$ docker-compose up` you instantiate all 3 services, which then can be accessed on a browser (`http://localhost:8080`).

If you configured the `SLACK_API_TOKEN` then you should also be able to use the bot on your Slack team account, out of the box! 📦

> Instructions on how to run each service separately can be found in each service folder.

## Deployment

This project is hosted on [Heroku](https://www.heroku.com/), **on just one dyno!**. Yup, 3 apps, different languages, one dyno. You can check it on [https://santosbot.herokuapp.com](https://santosbot.herokuapp.com).

The structure is pretty simple:
- There is an nginx app, working as reverse proxy, that redirects all requests to the frontend app;
- All "/api" request are proxied to the backend server;
- The actual bot is just running on a different process, and connects to my slack account using slack RTM library (yup, I have this live, working, just for the sake of it)
- Every process was started by honcho (foreman port to python) to bypass the number of dynos restriction on heroku.

There is actually a [blogpost](#) explaining how I achieved that, so you might just check that out 😄.

> If your curious commit [462b27a](https://github.com/andreffs18/santosbot/commit/462b27a) added all necessary files to make the app public, via heroku.
