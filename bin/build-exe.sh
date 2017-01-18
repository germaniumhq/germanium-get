#!/usr/bin/env bash

DOCKER_IMAGE="py2"
#DOCKER_IMAGE="cdrx/pyinstaller-windows:python2"

docker run -it \
    --rm \
    -v $(readlink -f $(dirname $(readlink -f "$0"))/..):/src \
    --link nexus \
    -e PYPI_URL="http://nexus:8081/repository/pypi-local/pyp" \
    -e PYPI_INDEX_URL="http://nexus:8081/repository/pypi-local/simple" \
    py2

