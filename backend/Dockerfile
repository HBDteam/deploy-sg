FROM --platform=linux/x86_64 python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

ADD requirements.txt /backend
ADD . /backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt