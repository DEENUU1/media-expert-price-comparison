FROM python:3.12

WORKDIR ../media_expert

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN addgroup --system media_expert && adduser --system --group media_expert

COPY config /media_expert/