#This program counts the distribution of the hour of the day for each of the messages. 
#You can pull the hour from the “From” line by finding the time string and then splitting 
#that string into parts using the colon character. Once you have accumulated the counts 
#for each hour, print out the counts, one per line, sorted by hour as shown below.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
hours = dict()
for line in fhand:
    words = line.split()

    if len(words) <= 5: continue
    if words[0] == 'From:': continue
    if words[0] == 'From':
        hour = words[5].split(':')[0]
        if hour not in hours:
            hours[hour] = 1
        else:
            hours[hour] += 1

lst = list()
for key, val in list(hours.items()):
    lst.append((val, key))
    lst.sort(reverse=True)
for key, val in lst:
    print(val, key)
