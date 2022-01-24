introduction = input ("introduce yourself - ")
characterCount = 0
wordCount = 1
print (introduction)
for i in introduction:
    characterCount = characterCount + 1
    if (i == ' '):
        wordCount = wordCount + 1
print ( characterCount )
print ( wordCount )