#Write a program to read through a mail log, build a histogram using a dictionary to count 
#how many messages have come from each email address, and print the dictionary.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    words = dict()
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    spl_lines = line.split()
    #print(spl_lines)
    if len(spl_lines) == 0: continue
    if spl_lines[0] == 'From:': continue
    if spl_lines[0] == 'From':
        #print(spl_lines[1])
        if spl_lines[1] not in words:
            words[spl_lines[1]] = 1
        else:
            words[spl_lines[1]] += 1

print(words)
