
# Lambda funtion to find square of a number
print("Lamda function to print square of a number")
sqr = (lambda n : n*n)(2)
print(sqr)

# Lambda function reusability
print("Lambda reusability: ")
square = (lambda n: n*n)
sqr1 = square(3)
sqr2 = square(5)
sqr3 = square(12)
print(sqr1)
print(sqr2)
print(sqr3)


# Lambda inside a function
print("\nLambda inside a function")
def func(n):
  return (lambda x : x*n)

math_calc = func(3)(5) 
print(math_calc)

# Reusing Lambda inside a function
print("Reusing lambda inside a function")
math_calc1 = func(3)
mul1 = math_calc1(4)
mul2 = math_calc1(6)
mul3 = math_calc1(7)
print(mul1)
print(mul2)
print(mul3)

# Lambda in for loop with function
print("\nLambda in for loop with function")
for i in range(1,11):
  print(math_calc1(i))

# Lambda with user input
num = int(input("Enter a number: "))
multiplier = func(num)
for i in range(1,11):
  print(f"{num} * {i} = {multiplier(i)}")