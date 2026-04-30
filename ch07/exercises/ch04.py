def mars_weight(number_in_family):
    total_mars_weight = 0
    for x in range(0, number_in_family):
        print('Please enter a family member\'s Earth weight')
        weight = float(input())
        total_mars_weight = total_mars_weight + (weight*0.3782)
    print(f'The total weight of your family on Mars is {total_mars_weight}')


mars_weight(3)
