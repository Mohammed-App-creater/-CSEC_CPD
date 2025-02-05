
word = input()
u = sum(1 for i in word if i.isupper())
l = sum(1 for i in word if i.islower())
print(word.upper() if u > l else word.lower())   