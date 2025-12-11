# ====== ETAP 1 – BUILDER ======
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app /app

# ====== ETAP 2 – TEST ======
FROM builder AS test

RUN pytest -q

# ====== ETAP 3 – FINAL ======
FROM python:3.12-slim AS final

WORKDIR /app

# копируем код + зависимости (сам код, не окружение)
COPY app /app

# ещё раз устанавливаем зависимости внутри final-образа
COPY app/requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# Запускаем приложение обычным Python, без gunicorn
CMD ["python", "-m", "src.app"]
