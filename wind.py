#!/usr/bin/env python3
from sys import argv
from os import popen
from os import system
from os.path import abspath
for w in range(2,len(argv)):
 if '/' in argv[w]:
#  argv[w]=abspath(argv[w])
  if system('wslpath -m '+argv[w]+'')==0:
   argv[w]=popen('wslpath -m '+argv[w]).read().strip()
q=' '.join(argv[1:])
print(q)
#system(q)
