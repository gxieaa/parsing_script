#!/usr/bin/env python
# encoding: utf-8

import sys

infile = sys.argv[1]
object_type = []
certain_type = []
with open(infile) as fi:
    for line in fi:
        split = line.split()
        num_type = split[1]
        for i in range(int(num_type)):
            #if split[2 + i] == 'truck':
            #    print split[0]
            #    certain_type.append(split[2 + i])
            # print split[2 + i]
            object_type.append(split[2 + i])
#print len(certain_type)
#print len(object_type)
#n = len(object_type)
#print n
#new_list = [ii for n, ii in enumerate(object_type) if ii not in object_type[:n]]
#print new_list
#print len(new_list)
