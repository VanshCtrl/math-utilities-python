A=input("Enter a Number: ")
list=[]
for i in range(1, int(A)+1):
    if int(A) % i == 0:
        list.append(i)
if len(list) == 2:
    print("The number is prime")
