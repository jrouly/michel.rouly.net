#!/usr/bin/env bash

set -euxo pipefail

gunicorn \
  -b :${APP_PORT:-5000} \
  --access-logfile - \
  --error-logfile - \
  web:app
