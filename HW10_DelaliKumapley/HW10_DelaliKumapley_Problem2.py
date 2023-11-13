#Delali Kumapley
#CS 100 H11
#Homework 10
#Due Date: November 16th

'''
Problem 2
Write a function named initialLetters that takes one parameter, wordList – a list of words. Create and return
a dictionary in which each initial letter of a word in wordList is a key and the corresponding value is a list
of the words in wordList that begin with that letter. There should be no duplicate words in any value in the
dictionary.
For example, the following is correct output:
print(initialLetters(horton))
{'I': ['I'], 's': ['say'], 'w': ['what'], 'm': ['mean'], 'a': ['and']}
'''

def initialLetters(wordList):
    myDict = {}
    for word in wordList:
        myDictKeys = myDict.keys()
        if word[0] in myDictKeys:
            if word not in myDict[word]:
                myDict[word[0]] = myDict[word[0]].append(word)
        else:
            myDict[word[0]] = [word]
    return myDict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))

horton2 = ['I', 'say', 'i', 'what', 'sassy', 'saturday', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton2))

horton3 = ['Amazing', 'grace', 'amazing', '!@', 'lovely', 'apple', 'Amazing!']
print(initialLetters(horton3))
