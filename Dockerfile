FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc wget gnupg2 ca-certificates && \
    apt-get install -y libnss3 libgconf-2-4 libxi6 libgdk-pixbuf2.0-0 libxcomposite1 libatk1.0-0 libxrandr2 libasound2 libatk-bridge2.0-0 libxshmfence1 && \
    apt-get install -y --no-install-recommends xvfb && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

RUN addgroup --system app && adduser --system --group app

COPY app/config /app/config

COPY .env /app/.env

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]