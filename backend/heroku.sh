#!/usr/bin/env bash
# Install poetry with specific version
pip install "poetry==1.0.5"
# Project initialization without creating virtalenv
poetry config virtualenvs.create false
poetry install $([ "$ENVIRONMENT" = 'production' ] && echo "--no-dev") --no-interaction --no-ansi
# Run project
uvicorn api:app --port 8888 --host 0.0.0.0