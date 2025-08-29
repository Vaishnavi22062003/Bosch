import sys
tot=0
k=len(sys.argv)
print("Size  =" , k)
print(sys.argv[0])
max=0
min=10
for i in range(1,k):
    if max<i:
        max=i
    if min>i:
        min=i
     
# for i in range(1,k):
#     tot=tot+ int(sys.argv[i])
 
print("max  =" , max, "min =",min)