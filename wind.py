''':'
python3 $0 $@
exit
':'''
from sys import argv
from os import getenv
home=getenv('HOME')
if home[-1]!='/':
	home+='/'
argv=[home+w[2:] if w.startswith('~/') else home if w=='~' else w] 
argv=[w if w[0] != '/' else w[5].upper()+':'+w[6:] if w.startswith('/mnt/') else '\\\\wsl$\\Ubuntu'+w for w in argv]
from subprocess import run
run(argv[1:])