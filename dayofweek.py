'''enter day of week and print name of day
if-elif-else
if condition:
    statement1
    statement2
elif:
    statement3
elif:
    statement4
...
else:
    statement5'''
day=int(input("enter day of week between 1 to 7:"))
if day ==1:
   print("The day is Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Enter valid week day")