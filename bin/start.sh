#!/usr/bin/env bash

set -euxo pipefail

gunicorn \
  -b :5000 \
  --access-logfile - \
  --error-logfile - \
  web:app
