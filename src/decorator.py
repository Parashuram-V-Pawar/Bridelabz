def outer(ref):
  def inner(a,b):
    if b==0:
      print("Error")
    else:
      ref(a,b)
  return inner

@outer
def div(a,b):
  print(a/b)

print(div(10,2))
print(div(10,0))