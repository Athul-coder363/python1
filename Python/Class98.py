def CountWordsFromFile():
    fileName = input("Enter the file name:")
    numberOfWords = 0
    f=open(fileName,"r")
    for l in f:
        words = l.split()
        print(words)
        numberOfWords+=len(words)
    print(len(words))
    print(numberOfWords)
CountWordsFromFile()        