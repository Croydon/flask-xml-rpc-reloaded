FROM mcr.microsoft.com/devcontainers/python:3.7

RUN apt-get update -y \
    && export DEBIAN_FRONTEND=noninteractive \
    && pip install --upgrade pip setuptools wheel

WORKDIR /workspace
