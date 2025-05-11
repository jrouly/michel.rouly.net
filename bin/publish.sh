#!/usr/bin/env bash

set -euxo pipefail

docker build . -t jrouly/michel.rouly.net:latest
docker push jrouly/michel.rouly.net:latest
