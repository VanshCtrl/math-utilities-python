A=input("Enter your Number: ")
A=int(A)
B=input("Enter your Number: ")
B=int(B)
C=input("Enter your Number: ")
C=int(C)

if A>B and A>C and C>B:
    print(f"Largest= {A}" f"Smallest= {B}" f"Middle= {C}")
elif B>A and B>C and C>A:
    print(f"Largest= {B}" f"Smallest= {A}" f"Middle= {C}")
else:
    print(f"Largest= {C}" f"Smallest= {A}" f"Middle= {B}")