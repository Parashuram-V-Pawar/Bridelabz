# Problem Statement:
# Write a Python program to calculate the wind chill based on temperature and wind speed.
#
# The program should take two double command-line arguments: 
#     t → temperature in Fahrenheit
#     v → wind speed in miles per hour
#
# The wind chill is calculated using the National Weather Service formula:
#     wind_chill = 35.74 + 0.6215*t + (0.4275*t - 35.75) * math.pow(v, 0.16)
#
# Constraints:
# - The formula is only valid if:
#       abs(t) <= 50
#       3 <= v <= 120
# - You may assume the input values are within the valid range.
#
# Instructions:
# - Use math.pow(a, b) to compute a^b.
# - Print the wind chill in a readable format.
#
#
import sys
import math

def wind_chill(t, v):
    wind = 35.74 + (0.6215 * t) + ((0.4275 * t - 35.75) * math.pow(v, 0.16))
    print(f"Wind Chill: {wind:.2f}")




if len(sys.argv) != 3:
    print("Usage: python windchill.py <x> <y>")
    sys.exit(1)

t = float(sys.argv[1])
v = float(sys.argv[2])

if abs(t) <= 50 and v >= 3 and v <= 120:
    wind_chill(t,v)
else: 
    print("Values must be less than 50 for temperature and in between 3 and 120 for velocity")