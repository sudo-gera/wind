#!/usr/bin/env python3
from os import *
from os.path import *
from sys import argv
q = str(abspath(dirname(argv[0])))+'/'
from subprocess import run
path='/usr/bin/wind'
if not exists(path):
	run(['sudo','ln','-s',q+'wind.py',pathbash]).returncode
	run(['sudo','chmod','777',path])
	