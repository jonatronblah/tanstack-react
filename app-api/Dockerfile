FROM python:3.11.6-slim-bookworm

RUN pip install poetry==1.7.1

WORKDIR /app

COPY pyproject.toml poetry.lock .

RUN poetry config virtualenvs.create false && \
    poetry install