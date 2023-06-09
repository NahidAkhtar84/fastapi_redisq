FROM python:3.11.2-alpine

RUN mkdir /app
WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r /app/requirements.txt
