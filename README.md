<h1 align="center">
  <a href="#">
    <img src="https://i.imgur.com/nM3mJd3.jpg" width="400">
  </a>
  <br><br>
</h1>

<h4 align="center">
    Slack Bot that spits out quotes from Gustavo Santos whenever a *Trigger Word* is written.
</h4>

<p align="center">  
  <a href="https://github.com/andreffs18/dotfiles/blob/master/LICENSE.md">
    <img src="https://img.shields.io/github/license/andreffs18/dotfiles?color=yellow&style=flat-square" />
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

```shell script
~ $ git clone git@github.com:andreffs18/santosbot.git
~ %

# Build and run project
~/santosbot $ docker-compose up --build
```


## Usage

This project had divided into 3 parts:

- [Backend API](/backend/README.md): Python ASGI web server that exposes an web API for getting Quoted.
- [Frontend App](/frontend/README.md): VueJS app that helps to showcase bot functionality.
- [Slack Bot](/bot/README.md): Actual slack bot that you can run to interact with.


