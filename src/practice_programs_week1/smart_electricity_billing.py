# "taking input for the program"
units = int(input())
bill = 0

# "creating a new variable and assigning value of units"
remaining_units = units

# "code logic for first 100 or below 100 units"
first = min(remaining_units, 100)
bill = bill + (first * 3)
remaining_units = remaining_units - first

# "code logic for next 100 or below 200 units"
second = min(remaining_units, 100)
bill = bill + (second * 5)
remaining_units = remaining_units - second

# "code logic for remaining units that are more than 200 units"
if remaining_units > 0:
  bill = bill + (remaining_units * 8)

# "checks condition if the units are exceeding 300 if yes it adds surcharge of 10%"
if units > 300 :
  bill += bill * 0.1

print(bill)