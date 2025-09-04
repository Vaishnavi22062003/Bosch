def remove_duplicates(l):
    res = []
    for val in l:
        if val not in res:
            res.append(val)
    return res
 
l1=input()
l1=list(map(int,l1.split()))
result=remove_duplicates(l1)
print(result)