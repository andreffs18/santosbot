# Backend API

Very simple HTTP web server build with on Python 3.7, using [Starlette](https://www.starlette.io/), an ASGI Framework.

Its main job is to expose an endpoint to return Gustavo Santos quotes 😂.

## Install 

Install docker and run the following:

```shell script
# Build and run project, on port 8888
~/santosbot/frontend $ docker build -e PORT=8888 -e ENVIRONMENT=development -t api:latest .
~/santosbot/frontend $ docker run --rm -it -v $(PWD):/app -p 8888:8888 api:latest 
```

## Usage

This api simple exposes two endpoints:

| Endpoint | Description |
| ----- | ----- | 
| **GET** `/version` | Return Api version | 
| **GET** `/bot?text="example sentence"` | Return quote, if available, for given `text` argument |  
