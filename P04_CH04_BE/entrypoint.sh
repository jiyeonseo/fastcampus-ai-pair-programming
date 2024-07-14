#!/bin/sh
export ENVIRONMENT=prod

poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080
