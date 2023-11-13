#Delali Kumapley
#CS 100 H11
#Homework 10
#Due Date: November 16th

'''
Problem 3
Write a function named shareOneLetter that takes one parameter,
wordList – a list of words. Create and return a dictionary in which each word in
wordList is a key and the corresponding value is a list of all the
words in wordList that share at least one letter with that word. There should be no duplicate words in any
value in the dictionary.
For example, the following is correct output:
print(shareOneLetter(horton))
{'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean', 'and'], 'mean': ['say', 'what', 'mean', 'and'],
'and': ['say', 'what', 'mean', 'and']}

'''

def shareOneLetter(wordList):
    myDict = {}
    compFile = wordList
    for word in wordList:
        myDict[word] = []
        for lett in word:
            for elem in compFile:
                if lett in elem:
                    if elem not in myDict[word]:
                        myDict[word].append(elem)

    return myDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton))


horton2 = ['Apple', 'apple', 'bananas', 'crazy', 'stud', 'cool', 'cooool']
print(shareOneLetter(horton2))

horton3 = ['Apple', 'apple', 'bananas', 'crazy', 'stud!', 'cool', 'cooool', '!thats me', '!']
print(shareOneLetter(horton3))