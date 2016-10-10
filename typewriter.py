#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from time import sleep

def typewriter(words):
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

typewriter('Hello world ...')