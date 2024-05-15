FROM postgres:16.1-bookworm


RUN apt-get update \
      && apt-get install git make gcc -y

RUN apt-get install postgresql-server-dev-16 -y


WORKDIR /tmp
RUN git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
WORKDIR pgvector
# RUN make
RUN make install
