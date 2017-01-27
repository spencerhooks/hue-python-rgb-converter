#!/usr/bin/python

try: import simplejson as json # Try to import simplejson, if not available use json
except ImportError: import json

import csv

with open('color_curves_rgb.csv', 'rU') as inputfile: # Read rgb color curves (csv file) into list
    results = list(csv.reader(inputfile))

rgb_list = [[int(x) for x in rec] for rec in results] # Convert the list to integers

def getXY(red, green, blue):
    X = red * 0.664511 + green * 0.154324 + blue * 0.162028;
    Y = red * 0.283881 + green * 0.668433 + blue * 0.047685;
    Z = red * 0.000088 + green * 0.072310 + blue * 0.986039;
    x = X / (X + Y + Z);
    y = Y / (X + Y + Z);
    return [x,y]

xy_list = []
for item, value in enumerate(rgb_list, start=0): # Convert each list element from RGB to XY
    xy_list.append(getXY(*rgb_list[item]))
    # print xy_list[item]

print xy_list

# with open('color_curves_xy_3.json', 'w') as outputfile: # Write list out to json file
#     json.dump(xy_list, outputfile)

# with open('color_curves_xy.json') as f: # Here as an example of how to read a json file into a list
#     xy_list2 = json.load(f)
#     print xy_list2
