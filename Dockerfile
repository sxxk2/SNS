FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /app
WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

COPY . ./