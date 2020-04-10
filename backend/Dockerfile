FROM python:3.7

ARG PORT
ENV PORT $PORT
ARG ENVIRONMENT
ENV ENVIRONMENT $ENVIRONMENT

ENV POETRY_VERSION=1.0.5 \
  # Prevent Python from writing *pyc files to disk
  PYTHONDONTWRITEBYTECODE=1 \
  # Dump Python tracebacks explicitly
  PYTHONFAULTHANDLER=1 \
  # Force STDOU & STDERR to be unbuffered
  PYTHONUNBUFFERED=1 \
  # Disable PIP Cache
  PIP_NO_CACHE_DIR=off \
  # Ignore warning check 
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  # Timeout for downloading packages
  PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

# Install poetry with specific version
RUN pip install "poetry==$POETRY_VERSION"
# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./
# Project initialization without creating virtalenv
RUN poetry config virtualenvs.create false && \
  poetry install $([ "$ENVIRONMENT" = 'production' ] && echo "--no-dev") --no-interaction --no-ansi
# Copying files and folder to root directory of the project:
COPY api ./api

EXPOSE $PORT
CMD uvicorn api:app --port $PORT --host 0.0.0.0
