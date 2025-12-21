# Problem Statement:
# Check whether the digits of a given number are strictly increasing
# from left to right.
#
# Definition:
# A number is said to have strictly increasing digits if each digit
# is greater than the digit immediately before it.
#
# Input:
# number    # integer value whose digits are to be checked
#
# Output:
# YES       # if digits are strictly increasing left to right
# NO        # otherwise
#
# Function to check the number pattern wheteher the numbers are in increasing order left to right.
def number_pattern_validator(number):
  # Converting number to string to traverse through the individual numbers
  num_string = str(number)
  # initializing a variable to keep track of number of elements traversed in while loop
  i=0
  # While loop iterates from i=0 till i == len(num_string)-2, ex: if we have 5 elements loop executes till 4th element
  while i < (len(num_string)-1):
    # Condition checks if current number is greater than next number, if Yes returns False, else increases number and checks again until all elements are checked
    if num_string[i] >=  num_string[i+1]:
      return False
    i += 1
  # If all elements fail the above if condition function returns True
  return True

# Input Statement, Expects user to enter a positive number
number = int(input("Enter a number: "))
# If user enters a negative number prints the message
if(number < 0):
  print("Plese enter positive integer")
else:
  # If user enters positive number, we are calling function to check the number pattern and printing "yes" if returned True else "no"
  print("YES") if number_pattern_validator(number) is True else print("NO")