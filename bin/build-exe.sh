#!/usr/bin/env bash

DOCKER_IMAGE="ciplogic/pyinstaller-windows:python3"

docker run -it \
    --rm \
    -v $(readlink -f $(dirname $(readlink -f "$0"))/..):/src \
    --link nexus \
    -e PYPI_URL="http://nexus:8081/repository/pypi-local/pyp" \
    -e PYPI_INDEX_URL="http://nexus:8081/repository/pypi-local/simple" \
    $DOCKER_IMAGE

