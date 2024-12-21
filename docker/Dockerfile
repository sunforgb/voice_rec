FROM python:3.11.5-slim-bookworm 

ENV PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    PYTHONDONTWRITEBYTECODE=1

RUN apt update && apt install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

#WORKDIR /project
#COPY poetry.lock pyproject.toml /project/

#RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi
