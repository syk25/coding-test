word = [x for x in input().strip()]

for i in range(len(word)):
    if word[i].isupper() == True:
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()

print(''.join(word))
