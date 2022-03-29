#Add code to the above program to figure out who has the most messages in the file. 
#After all the data has been read and the dictionary has been created, look through 
#the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to 
#find who has the most messages and print how many messages the person has.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    words = dict()
    largest = None
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

for key in words:
    if largest is None or key > largest :
        largest = key


#print(words)
print(largest, words[largest])
