#!/usr/bin/python

import sys

result = set()

if len(sys.argv) !=3:
    print("usage:<pmain> <fpath1> <fpath2>")
    sys.exit(-1)

fd1 = open(sys.argv[1],"r")
fd2 = open(sys.argv[2],"r")

for line in fd1.readlines():
    result.add(line)

for line in fd2.readlines():
    if line not in result:
        print(line[:len(line)-1])



fd1.close()
fd2.close()

