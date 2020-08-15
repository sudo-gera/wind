''':'
python3 $0 $@
exit
':'''
from sys import argv
arg0=argv[1]
argv=[w if w[0]=='-'  else w if w[0] != '/' else w[5].upper()+':'+w[6:] if w.startswith('/mnt/') else '\\\\wsl$\\Ubuntu'+w for w in argv]
if '/' not in arg0:
	argv[0]=arg0
from subprocess import run
run(argv)