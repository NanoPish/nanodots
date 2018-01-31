#!/bin/sh

muted=$(pamixer --sink 0 --get-mute)

if [ "$muted" = true ]; then
    echo "sound=MUTED"
else
    volume=$(pamixer --sink 0 --get-volume)

    if [ "$volume" -gt 49 ]; then
        echo "sound=$volume%"
    else
        echo "sound= $volume%"
    fi
fi
