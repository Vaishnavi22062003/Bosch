def Rotate_list(l1,k):
     k = k % len(l1)
     return l1[-k:]+l1[:-k]
l1=input()
l1=list(map(int,l1.split()))
k=int(input("Enter the position "))
result = Rotate_list(l1,k)
print(result)