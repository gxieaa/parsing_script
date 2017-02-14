#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import math

infile = sys.argv[1]
object_type = []
certain_type = []
center = []
distance = []
with open(infile) as fi:
    for line in fi:
        split = line.split()
        num_type = split[1]
        #print num_type
        for i in range(int(num_type)):
            #if split[2 + i] == 'truck':
            #    print split[0]
            #    certain_type.append(split[2 + i])
            # print split[2 + i]
            object_type.append(split[2 + i])
        for j in range(3 * int(num_type)):
            center.append(split[2 + 4 * int(num_type) + j])

for k in xrange(0, len(center), 3):
    distance.append(math.sqrt(k * k + (k + 1) * (k + 1)))
#print len(certain_type)
#print len(object_type)
for item in distance:
    print item
n = len(object_type)
print n
print len(center)
n_distance = len(distance)
print n_distance
unknow = []
bigMot = []
midMot = []
pedestrian = []
nonMot = []
smallMot = []
print '0 ~ 20m'
for i in range(len(distance)):
    if (distance[i] > float(0)) & (distance[i] < float(20)):
        print distance[i]
        if (object_type[i] == 'unknow'):
            unknow.append(object_type[i])
        if (object_type[i] == 'smallMot'):
            smallMot.append(object_type[i])
        if (object_type[i] == 'midMot'):
            midMot.append(object_type[i])
        if (object_type[i] == 'bigMot'):
            bigMot.append(object_type[i])
        if (object_type[i] == 'nonMot'):
            nonMot.append(object_type[i])

print 'unknow: %d' % len(unknow)
print 'bigMot: %d' % len(bigMot)
print 'midMot: %d' % len(midMot)
print 'pedestrian: %d' % len(pedestrian)
print 'nonMot: %d' % len(nonMot)
print 'smallMot: %d' % len(smallMot)
#print n
#new_list = [ii for n, ii in enumerate(object_type) if ii not in object_type[:n]]
#print new_list
unknow = []
bigMot = []
midMot = []
pedestrian = []
nonMot = []
smallMot = []
print '20 ~ 40m'
for i in range(len(distance)):
    if (distance[i] > float(20)) & (distance[i] < float(40)):
        print distance[i]
        if (object_type[i] == 'unknow'):
            unknow.append(object_type[i])
        if (object_type[i] == 'smallMot'):
            smallMot.append(object_type[i])
        if (object_type[i] == 'midMot'):
            midMot.append(object_type[i])
        if (object_type[i] == 'bigMot'):
            bigMot.append(object_type[i])
        if (object_type[i] == 'nonMot'):
            nonMot.append(object_type[i])

print 'unknow: %d' % len(unknow)
print 'bigMot: %d' % len(bigMot)
print 'midMot: %d' % len(midMot)
print 'pedestrian: %d' % len(pedestrian)
print 'nonMot: %d' % len(nonMot)
print 'smallMot: %d' % len(smallMot)
unknow = []
bigMot = []
midMot = []
pedestrian = []
nonMot = []
smallMot = []
print '40 ~ 60m'
for i in range(len(distance)):
    if (distance[i] > 40) & (distance[i] < 60):
        print distance[i]
        if (object_type[i] == 'unknow'):
            unknow.append(object_type[i])
        if (object_type[i] == 'smallMot'):
            smallMot.append(object_type[i])
        if (object_type[i] == 'midMot'):
            midMot.append(object_type[i])
        if (object_type[i] == 'bigMot'):
            bigMot.append(object_type[i])
        if (object_type[i] == 'nonMot'):
            nonMot.append(object_type[i])

print 'unknow: %d' % len(unknow)
print 'bigMot: %d' % len(bigMot)
print 'midMot: %d' % len(midMot)
print 'pedestrian: %d' % len(pedestrian)
print 'nonMot: %d' % len(nonMot)
print 'smallMot: %d' % len(smallMot)
#car = []
#van = []
#truck = []
#unknow = []
#bus = []
#bigMot = []
#midMot = []
#pedestrian = []
#nonMot = []
#Box = []
#smallMot = []
#for item in object_type:
#    if item == 'car':
#        car.append(item)
#    if item == 'van':
#        van.append(item)
#    if item == 'truck':
#        truck.append(item)
#    if item == 'unknow':
#        unknow.append(item)
#    if item == 'bus':
#        bus.append(item)
#    if item == 'bigMot':
#        bigMot.append(item)
#    if item == 'midMot':
#        midMot.append(item)
#    if item == 'pedestrian':
#        pedestrian.append(item)
#    if item == 'nonMot':
#        nonMot.append(item)
#    if item == 'Box':
#        Box.append(item)
#    if item == 'smallMot':
#        smallMot.append(item)
#
#print 'car: %d' % len(car)
#print 'van: %d' % len(van)
#print 'truck: %d' % len(truck)
#print 'unknow: %d' % len(unknow)
#print 'bus: %d' % len(bus)
#print 'bigMot: %d' % len(bigMot)
#print 'midMot: %d' % len(midMot)
#print 'pedestrian: %d' % len(pedestrian)
#print 'nonMot: %d' % len(nonMot)
#print 'Box: %d' % len(Box)
#print 'smallMot: %d' % len(smallMot)
