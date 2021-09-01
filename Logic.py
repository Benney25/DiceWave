import random
import math

# first step is to get the number of lines in the file and store as a var
file = open("corncob_caps.txt", "r")
z = 0
for line in file:
    if line != "\n":
        z += 1
file.close()

# second step is to return a random integer between 1 and variable, and store the results as a separate var
y = random.uniform(1, z)
x = math.floor(y)

# Third step is to use the new int to get a random word from the file.
# https://www.kite.com/python/answers/how-to-read-specific-lines-of-a-text-file-in-python
def getword():
    a_file = open("corncob_caps.txt")
    lines_to_read = [x]
    for position, line in enumerate(a_file):
        if position in lines_to_read:
            print(line)
    # file = open('corncob_caps.txt')
    # for position, x in enumerate(file):
    #     if 1 in x:
    #         print(x)

getword()


# the fourth step will be to eventually combine everything into a function that will be called (var) times