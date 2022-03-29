#Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
#Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, 
#print out the average spam confidence.


fname = input('Enter the file name: ')
try:
    fhand = open(fname, "r")
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    Line_without_spaces = line.replace(" ","")

    if Line_without_spaces.startswith('X-DSPAM-Confidence:'):
        #print(Line_without_spaces)
        start_number = Line_without_spaces.find(':')

        host = Line_without_spaces[start_number + 1:-1]
        host_float = float(host)
        count = count + 1
        total = total + host_float
        #print(host)
print("count is ", count)
print("total is ", total)
print("Average spam confidence:", total / count)
