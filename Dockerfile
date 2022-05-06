# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /musicalProject
COPY requirements.txt /musicalProject/
COPY .env /.env
RUN pip install -r requirements.txt
COPY . /musicalProject/
