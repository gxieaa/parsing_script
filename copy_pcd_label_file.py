#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import shutil
import random
label_filename = []
label_filename_infile = sys.argv[1]
train_source = '/home/xieguoyang/Downloads/pc_gt/point/pedestrian/pedestrian_train/'
label_source = '/home/xieguoyang/Downloads/pc_gt/point/pedestrian/train_label/'
train_destination = '/home/xieguoyang/Downloads/pc_gt/point/three_class/data/'
label_destination = '/home/xieguoyang/Downloads/pc_gt/point/three_class/label/'
i = 0
with open(label_filename_infile) as fi:
    for line in fi:
        line = line.strip()
        split = line.split('.')
        filename_str = split[0]
        filename_str = filename_str.split('/')
        filename = filename_str[1]
        print filename
        filename = filename + '.pcd'
        label = filename
        #filename = 'files/' + filename
        filename = train_source + filename
        #print filename
        label_filename.append(filename)
        shutil.copy(filename, train_destination)
        label = label_source + label + '.txt'
        shutil.copy(label, label_destination)
        i = i + 1
        #print i
        if i == 5000:
            break
        #pcd_filename.append(filename)

#print len(label_filename)
#train = []
#test = []
#size = 0.8
#split_point = int(len(label_filename) * size)
#train = random.sample(label_filename, split_point)
#for item in train:
#    shutil.move(item, train_destination)
