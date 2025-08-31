x = eval(input("enter values:"))
max = x[0]
min = x[0]
for i in x:
    if(i > max):
        max = i
    if(i < min):
        min = i
print("max",max)
print("min",min)
