def moon_weight():
    print('Please enter your current Earth weight')
    weight = float(input())
    print('Please enter the amount your weight might increase each year')
    increase = float(input())
    print('Please enter the number of years')
    years = int(input())
    years += 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print(f'Year {year} is {round(moon_weight, 4)}')


moon_weight()
