FROM python:3.9-slim-buster

RUN mkdir /code

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt 