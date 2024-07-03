#!/bin/bash
set -e

# Start Xvfb
Xvfb :99 -ac &
export DISPLAY=:99

exec "$@"