FROM python:3.8-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY wsgi.py .
COPY ./fakepay .

RUN [ "gunicorn", "-w 4", "wsgi:app"]
