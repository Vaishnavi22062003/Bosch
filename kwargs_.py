def fruits(**kwargs):
   total=0
   for v in kwargs.values():
       total+=v
   return total
print(fruits(apple=5, banana=8))
