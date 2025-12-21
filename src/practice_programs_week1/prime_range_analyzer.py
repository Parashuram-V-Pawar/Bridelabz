# Problem Statement:
# Print the count of prime numbers between two given integers A and B (inclusive).
#
# Input:
# A   # starting number of the range
# B   # ending number of the range
#
# Output:
# prime_count   # total number of prime numbers between A and B (inclusive)

# Function to check if the number is prime or not
def check_prime(num) :
  # check for negative numbers and 0, 1. and return false if number is less than 2
  if num < 2:
    return False
  # If the number is >2 then we proceed with prime check and return True if it is a prime or False.
  i = 2
  while( i*i <= num) :
    if(num % i == 0):
      return False
    i=i+1
  return True

# Function takes 2 parameters starting and ending and checks if prime numbers are present in this range.
def prime_range_analyzer(starting, ending):
  # Using count to keep track of number of prime numbers.
  count = 0
  # For loop to iterate through the numbers from starting to ending
  for i in range(starting, ending+1):
    # Sending the number to check_prime and expecting a return value and storing it in result
    result = check_prime(i)
    # Condition to check if the current number is prime or no, if yes increasing count by 1.
    if result is True :
      count += 1
  # Returning the total count value
  return count

# Input statement
starting = int(input("Enter starting number: "))
ending = int(input("Enter ending number: "))

# Passing value to function and printing the incoming response
print(prime_range_analyzer(starting, ending))