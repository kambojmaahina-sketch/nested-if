''''''
a=int(input("Enter Ram's age: "))
b=int(input("Enter Shyam's age: "))
c=int(input("Enter Mohan's age: "))
if a>b and a>c:
    print("Ram is the eldest.")
elif b>a and b>c:
    print("Shyam is the eldest.")
elif c>a and c>b:
    print("Mohan is the eldest.")
else:
    print("Two or more persons have the same highest age.")