FROM python:3.7-alpine

ENV TERM linux

run apk update && apk add --no-cache netcat-openbsd bash

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY exploit1.py /exploit1.py
COPY exploit2.sh /exploit2.sh

COPY check1.py /check1.py
