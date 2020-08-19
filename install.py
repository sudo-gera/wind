#!/usr/bin/env python3
from os import *
from os.path import *
from sys import argv
q=abspath(argv[0])
q=q[:-len(q.split('/')[-1])]
from subprocess import run
system(' '.join(['ln',q+'wind.py','~/.local/bin/wind']))
