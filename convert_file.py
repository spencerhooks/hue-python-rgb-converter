#!/usr/bin/python

try: import simplejson as json # Try to import simplejson, if not available use json
except ImportError: import json

import csv
from rgb_xy import Converter

converter = Converter()

with open('color_curves_rgb.csv', 'rU') as inputfile: # Read rgb color curves (csv file) into list
    results = list(csv.reader(inputfile))

rgb_list = [[int(x) for x in rec] for rec in results] # Convert the list to integers

xy_list = []
for item, value in enumerate(rgb_list, start=0): # Convert each list element from RGB to XY
    xy_list.append(converter.rgb_to_xy(*rgb_list[item]))
    # print xy_list[item]

# print xy_list

with open('color_curves_xy.json', 'w') as outputfile: # Write list out to json file
    json.dump(xy_list, outputfile)

# with open('color_curves_xy.json') as f: # Here as an example of how to read a json file into a list
#     xy_list2 = json.load(f)
#     print xy_list2
