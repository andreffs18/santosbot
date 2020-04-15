__version__ = "0.1.0"
import os
import logging
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route

from api.services import GetQuoteService
from api.quotes import TRIGGER_WORDS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


async def version(request):
    """Simple endpoint that exposes the backend project version"""
    return JSONResponse({"version": __version__})


async def bot(request):
    """From GET request parameters, extract "text" field and run it through our "Quote Finder" service"""
    try:
        quote = GetQuoteService(request.query_params.get("text")).call()
        return JSONResponse({"quote": quote}, 200)
    except KeyError:
        logger.debug(f'Error: failed to get "text" from HTTP body payload.')
        return JSONResponse({"error": '"text" field required.'}, 400)
    except RuntimeError as e:
        logger.debug(f'Error: invalid POST body message: {e}.')
        return JSONResponse({"error": "Invalid POST body message."}, 400)
    except Exception as e:
        logger.debug(f'Error: unexpected error: {e}.')
        return JSONResponse({"error": f"Unexpected error: {str(e)}"}, 500)


async def words(request):
    """From GET request, return dictionary of all trigger words and last time they were used.

    Since Starlette still doesnt serialize datetime objects (https://github.com/encode/starlette/issues/787),
    below we parse the datetime field to string."""
    response = {}
    for word, meta in TRIGGER_WORDS.items():
        response.update({
            word: str(meta.get("last_used_at"))
        })
    return JSONResponse(response, 200)


routes = [
    Route("/version", version),
    Route("/bot", bot),
    Route("/words", words)
]
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

environment = os.environ.get("ENVIRONMENT", "development")
debug = os.environ.get("DEBUG", True)
logger.info(f'🌀 Starting app in "{environment}" (DEBUG={debug})')
app = Starlette(debug=debug, routes=routes, middleware=middleware)
