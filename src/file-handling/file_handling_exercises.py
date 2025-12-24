# Creating a file
f = open("abc.txt","w")
f.write("Hi this python file handling exercise")
f.close()

# Reading a file
fr = open("abc.txt","r")
print(fr.read())
fr.close()

# Using with statement
with open("abc.txt") as f:
  print(f.read())
  f.write("Changes are done")
  f.seek(0)
  print(f.read())

