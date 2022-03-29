#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments


def count(word,letter):
    count = 0
    for _ in word:
        if _ == letter:
            count = count + 1
    print(count)

word_input = input('Enter your word\n')
letter_input = input('wich letter?\n')
count(word_input, letter_input)
