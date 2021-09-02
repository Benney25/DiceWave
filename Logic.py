import random
import math

def getword():

# get the number of newlines in the text file
    file = open("corncob_caps.txt", "r")
    z = 0
    for line in file:
        if line != "\n":
            z += 1
    file.close()

# pick a line from the file, store that line in a variable
    y = random.uniform(1, z)
    x = math.floor(y)

# use stored line to get the word on that line
    file = open("corncob_caps.txt")
    lines_to_read = [x]
    for position, line in enumerate(file):
        if position in lines_to_read:
            print(line)
    file.close()

# call the word (input-var), or (static-6) times.
def getpass():
    g = 0
    for i in range(6):
        getword()
        g += 1
    print(g)
getpass()