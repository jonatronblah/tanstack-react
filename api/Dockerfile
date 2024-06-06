FROM python:3.11.8-slim-bookworm as base

RUN apt-get update
RUN apt-get -y dist-upgrade

FROM base as requirements

RUN python3.11 -m pip install -U pip setuptools && \
    python3.11 -m pip install poetry==1.8.3

COPY api/pyproject.toml api/poetry.lock ./
RUN poetry export -f requirements.txt --without-hashes -o /requirements.txt 

FROM base as app

WORKDIR /usr/src/app

COPY --from=requirements /requirements.txt . 

RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

RUN apt-get purge -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*