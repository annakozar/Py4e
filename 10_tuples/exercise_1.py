#Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
#Count the number of messages from each person using a dictionary.

#After all the data has been read, print the person with the most commits by creating a list of (count, email) 
#tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.



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
    if len(spl_lines) <= 1: continue
    if spl_lines[0] == 'From:': continue
    if spl_lines[0] == 'From':
        # print(spl_lines[1])
        if spl_lines[1] not in words:
            words[spl_lines[1]] = 1
        else:
            words[spl_lines[1]] += 1

lst = list()
for key, val in list(words.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)
