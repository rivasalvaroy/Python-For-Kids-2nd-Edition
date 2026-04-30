def moon_weight(weight, increase, years):
    years += 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print(f'Year {year} is {round(moon_weight, 4)}')


moon_weight(35, 0.3, 5)
