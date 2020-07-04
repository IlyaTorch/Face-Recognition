FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
COPY ./app /app

RUN pip install -r requirements.txt

WORKDIR /app

RUN adduser --disabled-password --gecos '' user

USER user