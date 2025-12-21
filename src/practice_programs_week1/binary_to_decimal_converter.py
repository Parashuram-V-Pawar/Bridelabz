# Problem Statement:
# Convert a given binary number to its decimal equivalent without using built-in conversion functions.
#
# Input:
# binary_number   # a string or integer representing the binary number
#
# Output:
# decimal_number  # decimal equivalent of the given binary number
#
#
# Function to check whether the input received is binary
# If input is binary returns True else False
def is_binary(binary_num) :
  binary_num = str(binary_num)
  for ch in binary_num:
    if ch != "0" and ch != "1":
      return False
  return True

# Funtion to convert binary to decimal
def binary_to_decimal_converter(num) :
  remainder = 0
  decimal = 0
  i=0
  while num > 0:
    remainder = num%10
    decimal = decimal + (remainder * (2**i))
    num = num//10
    i += 1
  return decimal

# Input Statements
binary_num = int(input("Enter binary number: "))
# Condition to check whether the input is binary or no
if(is_binary(binary_num)):
  print(binary_to_decimal_converter(binary_num))
else:
  print("Please enter binary numbers in O's and 1's")