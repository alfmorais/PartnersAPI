FROM python:3.10

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN apt-get update && apt-get install -y \
    gnupg2 \
    ca-certificates \
    postgresql \
    postgresql-contrib \
    gcc \
    python3-dev \
    musl-dev

RUN apt-get clean && apt-get autoremove

WORKDIR /app

COPY pyproject.toml .

RUN pip install --upgrade pip \
    pip install poetry==1.5.0

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .
