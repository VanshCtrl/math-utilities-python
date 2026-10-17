Oddlist=[]
Evenlist=[]


for i in range(0,51,1):
    if i%2==0:
        Evenlist.append(i)
    else:
        Oddlist.append(i)

print("Even numbers:", Evenlist)
print("Odd numbers:", Oddlist)