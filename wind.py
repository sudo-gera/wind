''':'
python3 $0 $@
exit
':'''
from sys import argv
argv=[w if w[0] != '/' else w[5].upper()+':'+w[6:] if w.startswith('/mnt/') else '\\\\wsl$\\Ubuntu'+w for w in argv]
from subprocess import run
run(argv[1:])