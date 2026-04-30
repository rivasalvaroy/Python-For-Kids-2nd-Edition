'''For each year, you can calculate the new weight by adding a kilo-
gram and then multiplying by 16.5 percent (0.165)'''

weight = 30

for year in range(1, 16):
    weight += 1
    moon_weight = weight * 0.165
    print(f'Year {year} is {moon_weight}')
