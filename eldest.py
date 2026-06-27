'''enter age of ram shyam and mohan and print who is eldest suing if-elif-else'''
a=int(input("enter ram age:"))
b=int(input("enter shyam age:"))
c=int(input("enter mohan age:"))
if a>b and a>c:
    print("Ram is eldest")
elif a<b and b>c:
    print("Shyam is eldest")
elif a<c and c>b:
    print("Mohan is eldest")
else:
    print ("Two or more person have same age")