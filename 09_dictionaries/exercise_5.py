#This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
#(i.e., the whole email address). At the end of the program, print out the contents of your dictionary.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    words = dict()
    largest = None
    largest_address = ""
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    spl_lines = line.split()
    #print(spl_lines)
    if len(spl_lines) <= 1: continue
    if spl_lines[0] == 'From:': continue
    if spl_lines[0] == 'From':
        # print(spl_lines[1])
        if spl_lines[1] not in words:
            words[spl_lines[1]] = 1
        else:
            words[spl_lines[1]] += 1

for key in words:


    if largest is None or words[key] > largest :
        largest = words[key]
        largest_address = key


#print(words)
print(largest_address, largest)
