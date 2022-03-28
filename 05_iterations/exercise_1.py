
#Write a program which repeatedly reads numbers until the user enters “done”. 
#Once “done” is entered, print out the total, count, and average of the numbers. 
#If the user enters anything other than a number, detect their mistake using 
#try and except and print an error message and skip to the next number.


count = 0
total = 0
while True:
    raw_inp = input('Enter a number\n')
    if raw_inp == 'done':
        break
    try:
        inp = int(raw_inp)
    except:
        print('bad data')
        continue
    count = count + 1
    total = total + inp
print(total, count, total / count)
