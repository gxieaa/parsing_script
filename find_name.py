#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import shutil
import random
label_filename = []
label_filename_infile = sys.argv[1]
#source = '/home/xieguoyang/Downloads/pc_gt/point/'
#destination = '/home/xieguoyang/Downloads/pc_gt/point/pick_out_folder/'
with open(label_filename_infile) as fi:
    for line in fi:
        line = line.strip()
        split = line.split('.')
        filename_str = split[0]
        filename_str = filename_str.split('/')
        filename = filename_str[1]
        filename = filename + '.pcd'
        #filename = 'files/' + filename
        #filename = source + filename
        #print filename
        label_filename.append(filename)
        #shutil.copy(filename, destination)
        #pcd_filename.append(filename)

#print len(label_filename)
train = []
test = []
size = 0.8
split_point = int(len(label_filename) * size)
train = random.sample(label_filename, split_point)
#for item in range(0, split_point):
#    train.append(label_filename[item])
#print len(train)
#for i in train:
#    print i

for item in range(split_point, len(label_filename)):
    test.append(label_filename[item])
#print len(test)
for i in test:
    print i
