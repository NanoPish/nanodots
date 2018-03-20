#!/bin/sh

volume=$(pamixer --sink 0 --get-volume)
echo "$volume%"
