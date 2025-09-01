def bubble_sort(l1):
    n=len(l1)
    for i in range(n):
        swap=0
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                swap=1
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1
l1=input()
l1=list(map(int,l1.split()))
result=bubble_sort(l1)
print(result)