#Find all unique words in a file

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line)
    Lines_without_spaces = line.rstrip()
    #print( Lines_without_spaces)
    List_from_line = Lines_without_spaces.split()
    #print(List_from_line)
    for word in List_from_line:
        if word not in lst: lst.append(word)
lst.sort()
print(lst)
