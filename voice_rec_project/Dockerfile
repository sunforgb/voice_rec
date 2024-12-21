FROM python:3.11.5-slim-bookworm as builder

ENV PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    PYTHONDONTWRITEBYTECODE=1

RUN apt update && apt install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /voice_rec_project
COPY . /voice_rec_project/

RUN poetry install --no-interaction --no-ansi

