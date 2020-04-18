#!/usr/bin/env python3
from sys import argv
from os import popen
from os import system
from os.path import abspath
for w in range(2,len(argv)):
 if '/' in argv[w]:
  argv[w]=abspath(argv[w])
  argv[w]=popen('wslpath -m '+argv[w]).read()
q=' '.join(argv[1:])
print(q)
system(q)
