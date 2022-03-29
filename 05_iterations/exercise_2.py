#Write another program that prompts for a list of numbers as above and 
#at the end prints out both the maximum and minimum of the numbers instead of the average.


count = 0
total = 0
largest = None
smallest = None
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
    if largest is None or inp > largest :
        largest = inp
    if smallest is None or inp < smallest :
        smallest = inp
    
print(total, count, largest, smallest)
