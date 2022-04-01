#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
#Your program should convert all the input to lower case and only count the letters a-z. Your program 
#should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples 
#from several different languages and see how letter frequency varies between languages. Compare your 
#results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
letter_d = dict()
for line in fhand:
    line_only_alpha = ''.join(x for x in line if x.isalpha())
    line_without_spaces = line_only_alpha.replace(" ", "")
    line_without_spaces_lower = line_without_spaces.lower()
    list_of_letters = list(line_without_spaces_lower)
    for letter in list_of_letters:
        if len(list_of_letters) <= 0: continue
        if letter not in letter_d:
            letter_d[letter] = 1
        else:
            letter_d[letter] += 1
 
lst = list()
for key, val in list(letter_d.items()):
    lst.append((val, key))
    lst.sort(reverse=True)
for key, val in lst:
    print(val, key)
