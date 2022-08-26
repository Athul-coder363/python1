text = input("enter the string")
characterCount = 0
wordCount = 0
print(text)
for i in text:
    characterCount = characterCount+1
    if(i == ' '):
        wordCount = wordCount+1
print("Number of characters:",characterCount)
print("Number of words",wordCount)
        