

balance = int(input())
n = int(input())
arr = []

for i in range(n):
  arr.append(int(input()))

for i in range(n):
  if balance > arr[i] and arr[i] % 100 == 0:
    balance = balance - arr[i]
    print("SUCCESS")
  else:
    print("FAILED")
print(balance)