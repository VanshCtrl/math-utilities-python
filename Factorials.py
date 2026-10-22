A= int(input("Enter a number to find its factorial: "))

factorial_result = 1


if A< 0:
  print("Factorial does not exist for negative numbers.")
elif A== 0:
  print("The factorial of 0 is: 1")
else:
  for i in range(1, A + 1):
    factorial_result *= i 

  print(f"The factorial of {A} is: {factorial_result}")