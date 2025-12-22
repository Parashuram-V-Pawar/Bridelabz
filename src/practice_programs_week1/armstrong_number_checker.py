# Problem Statement:
# Check whether a given number is an Armstrong number.
#
# Definition:
# An Armstrong number is a number that is equal to the sum of the cubes
# of its digits. For example, 153 → 1³ + 5³ + 3³ = 153
#
# Input:
# number    # integer to be checked
#
# Output:
# YES       # if the number is an Armstrong number
# NO        # otherwise
#

# This function is used to count number of digits in the number
def no_of_digits(num) :
  count = 0
  while num > 0:
    num = num // 10
    count += 1
  return count

# Function to check for armstrong number
def armstrong_number_checker(number):
  # Creating new variable and assigning the number to it so that we can use it to compare later
  num = number
  armstrong = 0
  # Looping and performing calculation till the number is 0
  while num > 0:
    # First we are extracting last digit by using modulo operator 
    digit = num % 10
    # We are calculating cube of the digit extracted and adding it to the armstrong number
    armstrong = armstrong + (digit ** (no_of_digits(number)))
    # Performing integer division to remove last digit from the number
    num = num // 10
  # Once all the operations are done checking if number received and armstrong number has same value.
  # If the number is less than 10 by default it is considered as Armstrong number.
  # If yes print "YES" else print "NO"
  if number == armstrong:
    print("YES")
  else:
    print("No")

# Input statement, takes positive integer values as input
number = int(input("Enter a 3 digit integer: "))
# if the inout is negative prints error message else calls the function to check armstrong number
if number < 0:
  print("Negative numbers are not armstrong numbers.\nPlease enter positive number")
elif number > 0 and number < 10:
  print("YES")
elif number > 9 and number < 100:
  print("There ar no Armstrong numbers for 2 digit numbers")
else:
  armstrong_number_checker(number)
