vowels=0
consonants=0

for letter in input("give me a word and I will count the vowels and consonants for you: "):
    if letter.lower()in"aeiou":
        vowels=vowels+1
    elif letter=="":
        pass
    else:
        consonants=consonants+1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
