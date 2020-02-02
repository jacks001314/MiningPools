#!/bin/python

import sys

result = set()

if len(sys.argv) !=4:
    print("usage:<pmain> <fpath1> <fpath2> <out>")
    sys.exit(-1)

fd1 = open(sys.argv[1],"r")
fd2 = open(sys.argv[2],"r")
fd3 = open(sys.argv[3],"w+")

for line in fd1.readlines():
    result.add(line)

for line in fd2.readlines():
    result.add(line)

fd3.writelines(result)


fd1.close()
fd2.close()
fd3.close()
