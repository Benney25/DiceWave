import random
import math
#the first functionality we're going to deal with is going to be simplest first, more complicated concepts can be dealt with later


# First we need the line count
# https://www.kite.com/python/answers/how-to-get-a-line-count-of-a-file-in-python
file = open("corncob_caps.txt", "r")

z = 0

for line in file:

    if line != "\n":

        z += 1

file.close()


# Second, we need to select a random line from 1 to (var)
# https://careerkarma.com/blog/python-missing-required-positional-argument-self/
# was not instantiated, needed to call the variable being used before using it to create the range.
#https://pynative.com/python-random-randrange/
# was not implementing the numbers properly
# def wordselect():
y = random.uniform(1, z)
# https://www.w3schools.com/python/python_math.asp
x = math.floor(y)
# print(x)

# have to call the function on its own
# wordselect()


# Third step is to use the results from our new function to get a new word
def getword():
    file = open('corncob_caps.txt')
    for position, x in enumerate(file):
        if 1 in x:
            print(x)

getword()