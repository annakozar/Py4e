#Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this look for lines that start with “From”, then look for the third word and keep a running 
#count of each of the days of the week. At the end of the program print out the contents of your 
#dictionary (order does not matter)


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    words = dict()
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    #Lines_without_spaces = line.rstrip()
    #print( Lines_without_spaces)
    spl_lines = line.split()
    #print(spl_lines)
    if len(spl_lines) == 0: continue
    if spl_lines[0] == 'From:': continue
    if spl_lines[0] == 'From':
        #print(spl_lines)

            #print(spl_lines[2])
        if spl_lines[2] not in words:
            words[spl_lines[2]] = 1
        else:
            words[spl_lines[2]] += 1


print(words)
