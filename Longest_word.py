def longest_word(s):
    word=s.split()
    return max(word,key=len)
sentence=input()
print("Lomgest word : ", longest_word(sentence))