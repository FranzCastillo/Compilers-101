FROM ubuntu:22.04

RUN apt-get update -y \
  && apt-get install -y --no-install-recommends build-essential bison flex \
  && rm -rf /var/lib/apt/lists/*

COPY files /home/files
COPY programms /home/programms
COPY scripts /home

VOLUME /home
WORKDIR /home