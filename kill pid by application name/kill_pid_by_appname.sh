#!/bin/bash

# kill application by name
function killApp() {
    sudo pkill -f "app name"
}

# while loop
while true; do
    sleep 1  # 1 second wait
    killApp
done
