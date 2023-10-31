##Read the first section of Chapter 4 (Case Study: Interface Design): “The turtle module” in the
#textbook.
# Delali Kumapley
# CS 100 H11
# HW 03, September 28, 2023

'''1. Write code that uses turtle graphics to draw an equilateral triangle, a square and a regular pentagon,
each with side length 100.'''
import turtle as blueT 
import math
blueT_size = 100
blueT.color('blue')
blueT.width(10)
blueT.up()
blueT.goto(0,100)
blueT.down()
blueT.forward(blueT_size)
blueT.right(120)
blueT.forward(blueT_size)
blueT.right(120)
blueT.forward(blueT_size)
blueT.right(120)

redT = blueT.Turtle()
redT.color('red')
redT.width(5)
redT.up()
redT.goto(-200,150)
redT.down()

redT.fd(100)
redT.lt(90)
redT.fd(100)
redT.lt(90)
redT.fd(100)
redT.lt(90)
redT.fd(100)
redT.lt(90)

yellowT = blueT.Turtle()
yellowT.color('yellow')
yellowT.width(7)
yellowT.up()
yellowT.goto(200,-250)
yellowT.down()

yellowT.backward(100)
yellowT.rt(90)
yellowT.backward(100)
yellowT.rt(45)
yellowT.backward(100)
yellowT.lt(90)
yellowT.fd(100)
yellowT.lt(45)
yellowT.rt(90)
yellowT.fd(100)
yellowT.rt(90)
yellowT.fd(100)

'''
2. Write code that uses turtle graphics to draw four concentric circles of radius 50, 100, 150 and 200.'''

greenT = blueT.Turtle()
greenT.color('green')
greenT.width(4)

greenT.up()
greenT.goto(-200,-200)
greenT.down()
greenT.circle(50)
greenT.up()
greenT.goto(-200,-250)
greenT.down()
greenT.circle(100)
greenT.up()
greenT.goto(-200,-300)
greenT.down()
greenT.circle(150)
greenT.up()
greenT.goto(-200,-350)
greenT.down()
greenT.circle(200)


##3. Write code that uses the Python math module to compute and print out the values of
##a. 100!
print(math.factorial(100),'\n')

##b. the log (base 2) of 1,000,000
print(math.log2(1000000),'\n')

##c. the greatest common divisor of 63 and 49
print(math.gcd(63,49))
