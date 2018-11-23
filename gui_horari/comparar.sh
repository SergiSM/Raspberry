#!/bin/bash

if ! cmp -s $1 $2; then
  echo "files differ..."
  echo "sudo mv $2 $1"
  echo "python parser.py"
  echo "OBS PREV : download at sh not at py, py opens the new one. Only if it differs"
fi
