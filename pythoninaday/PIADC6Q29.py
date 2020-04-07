cities = {'Chicago': 'USA', 'New York City': 'USA', 'New Delhi': 'India', 'Seoul': 'South Korea',
          'Berlin': 'South Korea', 'London': 'United Kingdom', 'Shangai': 'China'}
city = input('Please enter a city name from above the list or enter End to exit:')
while city != 'End':
    try:
        print('%s is located in %s.\n' % (city, cities[city]))
    except:
        print('Sorry, no result found.\n')
    finally:
        city = input('Please enter a city name from above the list or enter End to exit:')
