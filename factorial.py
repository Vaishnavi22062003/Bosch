import math
x = int(input("enter number:"))
fact = 1
if x==0:
    print("fact is 0")
else:
    for i in range(1,x+1):
        fact = fact*i
print("factorial is ",fact)
