a_file = open("test_file.txt")

lines_to_read = [0, 2]

for position, line in enumerate(a_file):

    if position in lines_to_read:

        print(line)