# Problem Statement:
# Write a program to calculate the roots of a quadratic equation 
# of the form a*x*x + b*x + c = 0.
#
# Since the equation is quadratic (degree 2), it has exactly 2 roots.
#
# The two roots can be calculated using the quadratic formula:
#   delta = b*b - 4*a*c
#   Root 1 = (-b + sqrt(delta)) / (2*a)
#   Root 2 = (-b - sqrt(delta)) / (2*a)
#
# Input:
#   a, b, c   # coefficients of the quadratic equation
#
# Output:
#   root1, root2   # the two roots of the equation
#
import math
import cmath

def quadratic_equation(a, b, c):
  delta = (b*b) - (4 * a * c)

  # Real roots 
  if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Two distinct real roots: {root1}, {root2}")

  # Equal roots
  elif delta == 0:
    root1 = root2 = -b / (2*a)
    print(f"Two equal roots are: {root1}, {root2}")

  # Complex/Imaginary roots
  else:
    root1 = (-b + cmath.sqrt(delta)) / (2*a)
    root2 = (-b - cmath.sqrt(delta)) / (2*a)
    print(f"Two complex roots: {root1}, {root2}")

  


a = int(input("Enter the value of a: "))
if(a == 0):
  print("Enter positive value")
else:
  b = int(input("Enter the value of b: "))
  c = int(input("Enter the value of c: "))

  quadratic_equation(a, b, c)