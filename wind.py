#!/usr/bin/python3
from sys import argv
from os import getenv
home=getenv('HOME')
if home[-1]!='/':
	home+='/'
exe=argv[1]
argv=[home+w[2:] if w.startswith('~/') else home if w=='~' else w for w in argv] 
argv=[w if w[0] != '/' else w[5].upper()+':'+w[6:] if w.startswith('/mnt/') else '\\\\wsl$\\Ubuntu'+w for w in argv]
argv[1]=exe
from subprocess import run
run(argv[1:])