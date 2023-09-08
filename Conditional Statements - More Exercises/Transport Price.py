kilometers_traveled = int(input())
day_or_night = str(input())

taxi_start_cost = 0.70
taxi_day_tariff_cost = kilometers_traveled * 0.79
taxi_night_tariff_cost = kilometers_traveled * 0.90

bus_travel_cost = 0.09 * kilometers_traveled
train_travel_cost = 0.06 * kilometers_traveled

if kilometers_traveled < 20:
    if day_or_night == 'day':
        print(f'{taxi_day_tariff_cost + taxi_start_cost:.2f}')
    elif day_or_night == 'night':
        print(f'{taxi_night_tariff_cost + taxi_start_cost:.2f}')

if 20 <= kilometers_traveled < 100:
    print(f'{bus_travel_cost:.2f}')

if kilometers_traveled >= 100:
    print(f'{train_travel_cost:.2f}')