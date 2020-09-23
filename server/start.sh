#!/bin/sh -e

byobu new-session -d -s Server
byobu select-pane -t 0
byobu send-keys "go run ." Enter
byobu split-window -h
byobu send-keys "sleep 10" Enter
byobu send-keys "ffmpeg -re -stream_loop -1 -i test-images/ffmpeg/emptyvideo.ts -c copy -f rtsp rtsp://localhost:8554/mystream" Enter
exec byobu