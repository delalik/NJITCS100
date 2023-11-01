# Delali Kumapley
# CS 100 H11
# HW 08,November 2nd, 2023
'''
Read Chapter 7 (Iteration) in the textbook.
• Read the Python tutorial section 4.4 (break and continue Statements, and else Clauses on Loops).
The Python tutorial can be accessed through the documentation installed with IDLE:
Help  Python Docs  Tutorial  4. More Control Flow Tools
If you are using an alternate IDE, visit:
https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
to browse the tutorial online.
'''

'''
Problem 1
This problem provides practice using a while True loop.
Write a function named twoWords that gets and returns two words from a user. The first word is of a
specified length, and the second word begins with a specified letter.
The function twoWords takes two parameters:
1. an integer, length, that is the length of the first word and
2. a character, firstLetter, that is the first letter of the second word. The second word may begin with
either an upper or lower case instance of firstLetter.
The function twoWords should return the two words in a list. Use a while True loop and a break statement
in the implementation of twoWords.
The following is an example of the execution of twoWords:
print(twoWords(4, 'B'))
Enter a 4-letter word please: two
Enter a 4-letter word please: one
Enter a 4-letter word please: four
Enter a word beginning with B please: apple
Enter a word beginning with B please: pear
Enter a word beginning with B please: banana
['four', 'banana']
'''

def twoWords(length, firstLetter):
    perfectList = []
    while True:
        optWord1 = input("Enter a " + str(length) + "-letter word please: ")
        if(len(optWord1) == length):
            perfectList.append(optWord1)
            break

    while True:
        optWord2 = input("Enter a word beginning with " + firstLetter + " please: ")
        if(optWord2[0] == firstLetter.upper()) or (optWord2[0] == firstLetter.lower()):
            perfectList.append(optWord2)
            break
    print(perfectList)

##print(twoWords(4, 'B'))

'''
Problem 2
Write a function named twoWordsV2 that has the same specification as Problem 1, but implement it
using while and not using break. (Hint: provide a different boolean condition for while.)
Since only the implementation has changed, and not the specification, for a given input the output should
be identical to the output in Problem 1.
'''

def twoWordsV2(length, firstLetter):
    perfectList = []
    while len(perfectList) < 3:
        optWord1 = input("Enter a " + str(length) + "-letter word please: ")
        if(len(optWord1) == length):
            perfectList.append(optWord1)
            #pass
        optWord2 = input("Enter a word beginning with " + firstLetter + " please: ")
        if(optWord2[0] == firstLetter.upper()) or (optWord2[0] == firstLetter.lower()):
            perfectList.append(optWord2)

    print(perfectList)
#print(twoWords(4, 'B'))


'''
Problem 3
Write a function named enterNewPassword. This function takes no parameters. It prompts the user to
enter a password until the entered password has 8-15 characters, including at least one digit. Tell the
user whenever a password fails one or both of these tests.
'''
def enterNewPassword():
    lengthBool = False
    digitBool = False
    while not (lengthBool and digitBool):
        userPassword = input('Enter a password that is between 8 - 15 characters, including at least one digit\n')

        if 8 <= len(userPassword) <= 15:
            lengthBool = True
            for char in userPassword:
                if char.isnumeric():
                    digitBool = True
                    break
            if not digitBool:
                print("You need to have at least one digit in your password")
        else:
            print("Password length should be between 8 and 15 characters.")
    print("This password works!")

#enterNewPassword()



'''
Problem 4
Implement the GuessNumber game. In this game, the computer
• Think of a random number in the range 0-50. (Hint: use the random module.)
• Repeatedly prompt the user to guess the mystery number.
• If the guess is correct, congratulate the user for winning. If the guess is incorrect, let the user know if
the guess is too high or too low.
• After 5 incorrect guesses, tell the user the right answer.
The following is an example of correct input and output.
I'm thinking of a number in the range 0-50. You have five tries to guess it.
Guess 1? 32
32 is too high
Guess 2? 18
18 is too low
Guess 3? 24
You are right! I was thinking of 24!
'''

import random
def guessNumberGame():
    rand = random.randrange(0,50)
    print('I\'m thinking of a number in the range 0-50. You have five tries to guess it.\n')
    guessCount = 1
    while guessCount < 6:
        userGuess = input("Guess " + str(guessCount) + "? ")
        if(guessCount != 5):
            if(int(userGuess) == rand):
                print("You are right! I was thinking of " + str(rand) + "!")
                break
            elif(int(userGuess) > rand):
                print(userGuess + " is too high")
                guessCount += 1
            elif(int(userGuess) < rand):
                print(userGuess + " is too low")
                guessCount += 1

        else:
            if(int(userGuess) == rand):
                print("You are right! I was thinking of " + str(rand) + "!")
                break
            elif(int(userGuess) > rand):
                print(userGuess + " is too high. I was thinking of "+ str(rand) + "!, Game Over.")
                break

            elif(int(userGuess) < rand):
                print(userGuess + " is too low. I was thinking of "+ str(rand) + "!, Game Over.")
                break

##guessNumberGame()



