FROM python:3.7

ARG ENVIRONMENT=development

ENV \
  ENVIRONMENT=${ENVIRONMENT} \
  PROJECT_DIR=/app \
  POETRY_VERSION=1.0.5 \
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

WORKDIR $PROJECT_DIR

# Install poetry with specific version
RUN pip install "poetry==$POETRY_VERSION"
# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./
# Project initialization without creating virtalenv
RUN poetry config virtualenvs.create false && \
  poetry install $([ "$ENVIRONMENT" = 'production' ] && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY api ./api

EXPOSE 8888
CMD uvicorn api:app --port 8888 --host 0.0.0.0
