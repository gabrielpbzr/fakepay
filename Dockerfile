FROM python:3.9-slim-buster

ENV DATABASE_URL=postgres://fakepay:nAqpcZ3g4ax@database:5432/fakepay

COPY requirements.txt .
RUN apt-get update && apt-get install -y libpq-dev gcc 
RUN pip install -r requirements.txt

WORKDIR /app

COPY wsgi.py .
COPY ./fakepay /app/fakepay

RUN [ "gunicorn", "-w 4", "wsgi:app"]
