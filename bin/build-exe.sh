#!/usr/bin/env bash

docker run -it \
    --rm \
    -v $(readlink -f $(dirname $(readlink -f "$0"))/..):/src \
    --link nexus \
    cdrx/pyinstaller-windows:python2

