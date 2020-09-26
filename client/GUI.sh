#!/bin/sh -e
# "sudo xhost +" -> access control disabled, clients can connect from any host
# "export DISPLAY=:0" -> ur display

export DISPLAY=:0
docker run -it --rm -e DISPLAY=unix$DISPLAY --privileged -v /tmp/.X11-unix:/tmp/.X11-unix rtsp:client ffplay rtsp://172.17.0.2:8554/mystream
