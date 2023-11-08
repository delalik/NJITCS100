
## Delali Kumapley
## CS 100 H11
## Homework 09
##  November 9, 2023

'''
Problem 3
Write a function named repeat_words that takes two string parameters:
1. in_file: the name of an input file that exists before repeat_words is called
2. out_file: the name of an output file that repeat_words creates

Assume that the input file is in the current working directory and write the output file to that directory.
For each line of the input file, the function repeat_words should write to the output file all of the words
that appear more than once on that line. Each word should be lower cased and stripped of leading and
trailing punctuation. Each repeated word on a line should be written to the corresponding line of the
output file only once, regardless of the number of times the word is repeated.
For example, if the following is the content of the file catInTheHat.txt:
Too wet to go out and too cold to play ball.
So we sat in the house.
We did nothing at all.
So all we could do was to Sit! Sit! Sit! Sit!
The following function call:
inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)
should create the file
catRepWords.txt with the content:
    too to
sit
Hint: Be sure to test your solution with input in which some repeated words on a line are a mixture of upper
and lower case, and in which repeated words sometimes are preceded or followed by punctuation.
'''

def repeatWords(in_file, out_file):
    inFile = open(in_file, 'r')
    outFile = open(out_file, 'w')
    content = inFile.readlines()
    import string

    finalDict = {}
    count = 0
    for line in content:
        wordsDict = {}
        count +=1
        for word in line.split():
            if word.islower():
                if word in wordsDict:
                    wordsDict[word] += 1
                else:
                    wordsDict[word] = 1
            else:
                word = word.lower()
                if word in wordsDict:
                    wordsDict[word] += 1
                else:
                    wordsDict[word] = 1
        for word in wordsDict:
            if wordsDict[word] > 1:
                finalDict[word] = count

    prevValue = None
    for key in finalDict:
        if finalDict[key] == prevValue:
            outFile.write(key.strip(string.punctuation) + " ")
        else:
            outFile.write('\n' + key.strip(string.punctuation) + " ")

        prevValue = finalDict[key]


print(repeatWords('cat.txt', 'catOut.txt'))
