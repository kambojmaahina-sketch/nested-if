'''Biggest between 3 num using if-elif-else and logical operators'''
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("a is the biggest num.")
elif b>a and b>c:
    print("b is the biggest num.")
elif c>a and c>b:
    print("c is the biggest num.")
else:
    print("Two or more numbers have the same highest value.")