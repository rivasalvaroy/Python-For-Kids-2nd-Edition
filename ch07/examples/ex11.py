import sys


def silly_age_joke():
    age = int(input('How old are you?\n'))

    if age >= 10 and age <= 13:
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')
    else:
        print('Huh?')


silly_age_joke()
