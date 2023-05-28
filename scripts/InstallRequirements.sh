#!/bin/sh

sudo apt-get update && apt-get install -y \
    gnupg2 \
    ca-certificates \
    postgresql \
    postgresql-contrib \
    gcc \
    python3-dev \
    musl-dev