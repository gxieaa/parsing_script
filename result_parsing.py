#!/usr/bin/env python
# encoding: utf-8
import json
import sys

infile = sys.argv[1]
num_bbox = []
object_type = []
with open(infile) as fi:
    for line in fi:
        split = line.split('\t')
        filename = split[2]
        json_str = split[3]
        data = json.loads(json_str)
        tem_str = filename[8:]
        if data['result'] == '':
            continue
        for item in data['result']:
            object_type.append(item['type'])
            num_bbox.append(item['globalID'])
        tem_str = tem_str + ' ' + str(len(num_bbox)) + ' '
        for item_type in object_type:
            tem_str = tem_str + ' ' + item_type
        tem_str = tem_str + ' '
        for item in data['result']:
            tem_str = tem_str + item['rotation']['phi'] + ' '
            tem_str = tem_str + item['rotation']['theta'] + ' '
            tem_str = tem_str + item['rotation']['psi'] + ' '
        tem_str = tem_str + '\t'
        for item in data['result']:
            tem_str = tem_str + item['position']['x'] + ' '
            tem_str = tem_str + item['position']['y'] + ' '
            tem_str = tem_str + item['position']['z'] + ' '
        tem_str = tem_str + '\t'
        for item in data['result']:
            tem_str = tem_str + item['size'][0] + ' '
            tem_str = tem_str + item['size'][1] + ' '
            tem_str = tem_str + item['size'][2] + ' '
        print tem_str
        object_type = []
        num_bbox = []
