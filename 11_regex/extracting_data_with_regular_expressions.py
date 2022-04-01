#Using Python to Access Web Data
#week 2
#Extracting Data With Regular Expressions


import re

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    total = 0

except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    a_string = "".join(x)
    if len(x) > 0:
        results = [int(i) for i in x]

        if len(results) > 1:
            total_for_line = sum(results)
            total = total + total_for_line
        if len(results) == 1:
            an_integer = int(a_string)
            total = total + an_integer
print(total)_
