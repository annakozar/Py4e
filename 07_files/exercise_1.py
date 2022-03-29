#Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fname = input('Enter the file name: ')
try:
    fhand = open(fname, "r")
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    print(line.upper().rstrip())
