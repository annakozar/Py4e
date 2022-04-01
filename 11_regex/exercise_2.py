#Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method. 
#Compute the average of the numbers and print out the average as an integer.


import re
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    words = dict()
    count = 0
    total = 0

except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    line = line.rstrip()
    x = re.findall('^N.*: ([0-9]+)', line)
    a_string = "".join(x)
    if len(a_string) > 0:
        an_integer = int(a_string)
        count = count + 1
        total = total + an_integer

print (int(total/count))
