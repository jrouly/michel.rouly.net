#!/usr/bin/env bash

set -euxo pipefail

flask --app web:app run
