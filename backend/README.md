# Backend API

Very simple HTTP web server build on Python 3.7, using [Starlette](https://www.starlette.io/), an ASGI Framework.

Its main job is to expose an endpoint to return Gustavo Santos quotes 😂.

## Install 

To just run the backend api you must install [docker](https://docs.docker.com/get-docker/) and run the following:

```shell script
# Build and run project, on port 8888
~/santosbot/backend $ docker build --build-arg PORT=8888 --build-arg ENVIRONMENT=development -t backend:latest .
~/santosbot/backend $ docker run --rm -it -v $(PWD):/app -p 8888:8888 backend:latest 
```

## Usage

This api exposes three endpoints:

| Endpoint | Description |
| ----- | ----- | 
| **GET** `/version` | Return Api version | 
| **GET** `/words` | Return key-value pair of all available "trigger words", with the value being the last time it was used |
| **GET** `/bot?text="example sentence"` | Return quote, if available, for given `text` argument |  


### How does it work?

Simply put the logic behind the `/bot` endpoint is the following:

```mermaidjs
graph TD
	A[GET /bot?text=Hello World] --> B
	B[Get 'text' params from <br>request args and split<br> into 'tokens'] --> C
    C{Intersect 'tokens' <br>with 'TRIGGER_WORDS'}
	C --> |No intersection<br>found| D
	C --> |Found intersection| E
    D[Return empty quote]
    E[Get random 'TRIGGER_WORD'<br>from intersection] --> F
    F[Get random quote <br>associated with 'TRIGGER_WORD'] --> G
    G{Was quote used in <br>the last X seconds?}
    G --> |Yes| D
    G --> |No| H
    H[Update 'last_used_at' date for given quote] --> I
    I[Return quote]
```

> All quotes were generated using the [jupyter notebook](https://jupyter.org/) file on **"/backend/utils/Gustavo Santos Quote Extractor.ipynb"**, 
which is simply extracting all quotes found on http://www.citador.pt/frases/citacoes/a/gustavo-santos/ and creating the dictionary found on **"/backend/api/quotes.py"**