#!/bin/bash

exec python3 ./dataset.py &
exec python3 ./train.py &