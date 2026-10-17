A=int(input("Enter a Number: "))
list=[]
for i in range(1, int(A)):
    if int(A) % i == 0:
        list.append(i)
if sum(list) == A:
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")
