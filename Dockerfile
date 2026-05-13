#FROM python:3.14-slim
#
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#RUN apt-get update\
#    && apt-get install -y --no-install-recommends \
#--no-install-recommends\
#    build-essential\
#    libpq-dev\
#    && rm -rf/var/lib/apt/lists/*
#
#COPY pyproject.toml uv.lock./
#
#RUN pip install --no-cache-dir uv \
#    && uv pip install --system --no-cache -r pyproject.toml \
#    && pip install --no-cache-dir gunicorn
#
#COPY . .
#
#RUN mkdir -p/app/staticfiles
#
#EXPOSE 8000
#
#CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn QuickPay.wsgi:application --bind 0.0.0.0:8000"]

#
#FROM python:3.14-slim
#
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libpq-dev \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY pyproject.toml uv.lock ./
#
#RUN pip install --no-cache-dir uv \
#    && uv pip install --system . \
#    && pip install --no-cache-dir gunicorn
#
#COPY . .
#
#RUN mkdir -p /app/staticfiles
#
#EXPOSE 8000
#
#CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn QuickPay.wsgi:application --bind 0.0.0.0:8000"]


FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn

COPY . .

RUN mkdir -p /app/staticfiles

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn QuickPay.wsgi:application --bind 0.0.0.0:8000"]