<h1 align="center">
  <a href="#">
    <img src="https://i.imgur.com/nM3mJd3.jpg" width="400">
  </a>
  <br><br>
</h1>

<h4 align="center">
    Slack Bot that spits out quotes from Gustavo Santos whenever a *<a href="https://santosbot.herokuapp.com/words/" target="_blank" >Trigger Word</a>* is written.
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
    <a href="#usage">Usage</a>
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

If you configured the `SLACK_API_TOKEN` then you should also be able to use the bot on your Slack team account.


