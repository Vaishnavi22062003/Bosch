x = input("enter string:")
vowels=0
consonants=0
for i in x:
    if(i=='a' or i=='e' or i=='o' or i=='u' or i=='i'):
        vowels+=1
    else:
        consonants+=1
print("count of vowels:", vowels)
print("count of consonants:", consonants)
