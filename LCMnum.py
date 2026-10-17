A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

maximum = max(A, B)

for i in range(maximum, (A * B) + 1):
  if i % A == 0 and i % B == 0:
    print("The LCM is:", i)
    break  