# -*- coding: utf-8 -*-
import json
import sys


result = set()

if len(sys.argv)!=4:
    print("usage:<pmain> <fpath> <type> <out>")
    sys.exit(-1)

fd = open(sys.argv[1],'r')

types = sys.argv[2]

fdd = open(sys.argv[3],'w+')


for line in fd.readlines():
    s = json.loads(line)
    if s['type'] == types:
        result.add(s['value']+'\n')

fdd.writelines(result)
fdd.close()

