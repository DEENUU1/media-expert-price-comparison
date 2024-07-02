FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb


COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

RUN addgroup --system app && adduser --system --group app

COPY app/config /app/config
COPY .env /app/.env