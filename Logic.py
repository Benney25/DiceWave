import random
import math

def getnum():
    num = random.uniform(1, 99)
    num = math.floor(num)
    return (num)

def getdelimit():

# get the number of newlines in the text file
    file = open("delimiters.txt", "r")
    z = 0
    for line in file:
        if line != "\n":
            z += 1
    file.close()

# pick a line number from the file, store that line number in a variable
    y = random.uniform(1, z)
    x = math.floor(y)

# use stored line to return the content on that line
    file = open("delimiters.txt")
    lines_to_read = [x]
    for position, line in enumerate(file):
        if position in lines_to_read:
            delimiter = line.rstrip('\r\n')
            return(delimiter)
    file.close()

def getword():

# get the number of newlines in the text file
    file = open("corncob_lowercase.txt", "r")
    z = 0
    for line in file:
        if line != "\n":
            z += 1
    file.close()

# pick a line from the file, store that line in a variable
    y = random.uniform(1, z)
    x = math.floor(y)

# use stored line to return the content on that line
    file = open("corncob_lowercase.txt")
    lines_to_read = [x]
    for position, line in enumerate(file):
        if position in lines_to_read:
            word = line.rstrip('\r\n')
            return(word)
    file.close()

# call the word (input-var), or (static-6) times and concatenate each call to the end of the resulting string.
def getstr():
    f = str(getnum())
    g = str(getword())
    h = str(getdelimit())
    # for i in range(6):
    j = f + g + h
    return(j)

# why does this function work this way and not with r = r + r?
# is there any way I can get this to work without needing to use str on every func call?
# why do I need to use str on every func call for this func to work?
def getpass():
    r = str(getstr())
    for i in range(2):
        r = r + str(getstr())
    return (r)


print(getpass())