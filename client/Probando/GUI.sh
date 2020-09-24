#!/bin/sh -e

docker run --rm - it -e DISPLAY=$(DISPLAY) -v /tmp/.X11-unix:/tmp/.X11-unix  rtsp:client
