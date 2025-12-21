# Problem Statement:
# Given a number, count how many times it can be divided by 2 until it becomes odd.
#
# Input:
# number   # an integer greater than 0
#
# Output:
# count    # total number of times the number can be evenly divided by 2
#
# Function to compress the number by dividing the number by 2 and return the number of times it can be divided till it becomes odd
def number_compression_counter(number):
  count=0
  # This statements loops till the number becomes odd
  while number % 2 == 0:
      number = number/2
      count += 1
  return count

# Input statement
number = int(input("Enter a number: "))
# Condition to check for positive number
if number <= 0:
  print("Enter number greater than 0")
else :
  print(number_compression_counter(number))