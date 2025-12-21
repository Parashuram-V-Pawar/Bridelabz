# Problem Statement:
# Write a Python program to calculate the Euclidean distance from a point (x, y) to the origin (0, 0).
#
# The program should take two integer command-line arguments: x and y.
#
# The Euclidean distance is calculated using the formula:
#     distance = sqrt(x*x + y*y)
#

import math
import sys

def euclidean_distance(x,y):
  distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
  print(f"Distance from ({x},{y}) to origin: {distance}")

if len(sys.argv) != 3:
    print("Usage: python distance.py <x> <y>")
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])
euclidean_distance(x,y)