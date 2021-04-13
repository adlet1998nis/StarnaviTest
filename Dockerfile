FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y build-essential

COPY requirements/ /tmp/requirements

RUN pip install -r /tmp/requirements/base.txt

COPY . /code

WORKDIR /code
