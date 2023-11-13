#Delali Kumapley
#CS 100 H11
#Homework 10
#Due Date: November 16th

'''
Problem 1
Write a function named initialLetterCount that takes one parameter, wordList — a list of words. Create and
return a dictionary in which each initial letter of a word in wordList is a key and the corresponding value
is the number of words in wordList that begin with that letter. The keys in the dictionary should be case-sensitive, which means 'a' and 'A' are two different keys.
For example, the following is correct output:
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))
{'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}
'''

def initialLetterCount(wordList):
    myDict = {}
    for word in wordList:
        dictKeys = myDict.keys()
        if word[0] in dictKeys:
            myDict[word[0]] += 1
        else:
            myDict[word[0]] = 1
    return myDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

horton2 = ['I', 'say', 'What', 'i', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton2))

horton3 = ['Apples', 'applez', 'Apples', 'bananas', 'applez', 'angel', 'angle', 'Boo!', '!', 'cat']
print(initialLetterCount(horton3))

