## Delali Kumapley
## CS 100 H11
## Homework 09
##  November 9, 2023

'''
Problem 2
Write a function named file_stats that takes one string parameter (in_file) that is the name of an existing
text file. The function file_stats should calculate three statistics about in_file: the number of lines it
contains, the number of words and the number of characters, and print the three statistics on separate
lines. For example, the following would be correct input and output:
#>>> file_stats('created_equal.txt')
lines 2
words 13
characters 72
Note: The number of characters may vary slightly between operating systems. Similarly, the number of lines
may vary by 1 line, depending on the method used to calculate it.
'''

def file_stats(in_file):
    myFile = open(in_file, 'r+')
    lineCount = 0
    wordCount = 0
    charCount = 0


    lst = myFile.readlines()
    lineWordLst = []
    for line in lst:
        lineCount += 1

    for elem in lst:
        for char in elem:
            if char == ' ':
                charCount +=1

    myFile.close()


    import string

    myFile2 = open(in_file, 'r+')
    fileStr = myFile2.read()

    fileStr.strip(string.punctuation)
    fileStr.replace('-', ' ')
    strLst = fileStr.split()

    for word in strLst:
        wordCount+=1
        # print(word)
        for char in word:
            charCount +=1



    return "lines: " + str(lineCount) + "\nwords: " + str(wordCount) + "\ncharacters: " + str(charCount)



#print(file_stats('created_equal.txt'))