#Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
#It doesn’t matter what the values are. Then you can use the in operator as a fast way to 
#check whether a string is in the dictionary.


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
    for word in spl_lines:
     if word not in words:
            words[word] = 1

print(words)
