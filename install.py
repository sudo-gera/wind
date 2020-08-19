#!/usr/bin/env python3
from os import *
from os.path import *
from sys import argv
q=abspath(argv[0])
q=q[:-len(q.split('/')[-1])]
a=system('ln '+q+'wind.py ~/.local/bin/wind')
