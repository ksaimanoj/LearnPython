def printDictionary(n):
    dictionary = {}
    for i in range(1, n):
        dictionary[i] = i*i
    print(dictionary)

printDictionary(100)