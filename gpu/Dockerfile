FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04 as base

ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME=/gpu_backend/poetry
ENV POETRY_CACHE_DIR=/gpu_backend/.poetry_cache


ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y wget build-essential libncursesw5-dev libssl-dev && \
    apt-get install -y libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y python3.11 python3-pip


FROM base as requirements

RUN python3.11 -m pip install -U pip setuptools && \
    python3.11 -m pip install poetry==${POETRY_VERSION}



COPY gpu/pyproject.toml gpu/poetry.lock ./ 
RUN poetry config virtualenvs.create false
RUN poetry install

# RUN poetry export -f requirements.txt --without-hashes -o /requirements.txt 

# FROM base as app
# RUN python3.11 -m pip install -U pip setuptools

# COPY --from=requirements /requirements.txt . 

# RUN python3.11 -m pip install --no-cache-dir -r requirements.txt


# RUN pip install llama-cpp-python \
#     --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121




RUN apt-get purge -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*
