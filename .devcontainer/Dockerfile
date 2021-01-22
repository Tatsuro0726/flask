FROM python:3

RUN apt-get upgrade &&\
    pip install --upgrade pip

ENV FLASK_APP=src
ENV FLASK_ENV=development

WORKDIR /app
