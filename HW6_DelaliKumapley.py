## Delali Kumapley
## HW6 CS100 H11
## October 19th, 2023
'''
1a. Write a function named hasFinalLetter that takes two parameters
1. strList, a list of non-empty strings
2. letters, a string of upper and/or lower case letters
The function hasFinalLetter should create and return a list of all the strings in strList that end with a letter in letters.
'''

def hasFinalLetter(strList, letters):
  ##strList = ['hello', 'world', 'beautiful', 'cat']
 ## letters = 'aUndoGRWSjwfUFhs'
  finalLst = []

  for word in strList:
    finLet = word[len(word)-1]
    if finLet in letters:
       finalLst.append(word)

  return finalLst
    

'''
1b. Create three test cases, each consisting of a list of non-empty strings and a string of upper and/or lower case letters, for your function in Problem 1a. One of these tests should return the empty list. For each test case write two assignment statements and a function call that pass the test arguments to your function.
'''

myLst = ["hello", 'adieu', "goodbye", "greetings", "howdy"]
lets = 'aeiouU'
myLst2 = ["GOOD DAY", 'SALUTATIONS', 'HOW ARE YOU']
lets2 = 'AEIOU'
myLst3 = ['guten tag', 'morning' ]
lets3 = 'aeiouAEIOU'
print(hasFinalLetter(myLst, lets))
print(hasFinalLetter(myLst2, lets2))
print(hasFinalLetter(myLst3, lets3))

'''
2a. Write a function named isDivisible that takes two parameters
1.maxInt, an integer
2.twoInts, a tuple of two integers

The function isDivisible should create and return a list of all the ints in the range from 1 to maxInt (not including maxInt) that are divisible of both ints in twoInts.

'''
def isDivisible(maxInt, twoInts):
  finalLst = []
  for i in range(1,maxInt):
    if(i % twoInts[0] == 0) and (i % twoInts[1] == 0):
      finalLst.append(i)
        
  return finalLst

'''
2b. Create three test cases, each consisting of a value for
maxInt and a value for twoInts, for your function in Problem 2a. One of these tests should return the empty list. For each test case write two assignment statements and a function call that pass the test arguments to your function.

'''

num = 20
tup = (5, 10)
print(isDivisible(num, tup))

num2 = 1000
tup2 = (50, 25)
print(isDivisible(num2, tup2))

num3 = 25
tup3 = (15, 17)
print(isDivisible(num3, tup3))
