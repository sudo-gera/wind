#!/usr/bin/python3
from sys import argv
from os import getenv
from os.path import exists
from os import popen
home=getenv('HOME')
if home[-1]!='/':
	home+='/'
root=''
while not exists(home+'.windroot'):
	open(home+'.windroot','w').write('\\\\wsl$\\'+popen('echo `bash -c "cd /; powershell.exe -c \\"(Get-Location).tostring()\\""`').read().split('\\wsl$\\',1)[1])
root=open(home+'.windroot').read().strip()
if root and root[-1] in '/\\':
	root=root[:-1]
exe=argv[1]
argv=[home+w[2:] if w.startswith('~/') else home if w=='~' else w for w in argv]
argv=[w if w[0] != '/' else w[5].upper()+':'+w[6:] if w.startswith('/mnt/') else root+w for w in argv]
argv[1]=exe
from subprocess import run
run(argv[1:])
