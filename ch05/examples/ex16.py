age = '10.5'

# ValueError: invalid literal for int() with base 10: '10.5'
converted_age = int(age)

if converted_age == 10:
    print("What's the best way to speak to a monster?")
    print("From as far away as possible!")
