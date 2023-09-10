budget = float(input())
season = str(input())

car_type = ''
car_class = ''
car_cost = 0


if budget <= 100:
    car_class = 'Economy class'

    if season == 'Summer':
        car_type = 'Cabrio'
        car_cost = budget * 0.35

    elif season == 'Winter':
        car_type = 'Jeep'
        car_cost = budget * 0.65

elif 100 < budget <= 500:
    car_class = 'Compact class'

    if season == 'Summer':
        car_type = 'Cabrio'
        car_cost = budget * 0.45

    elif season == 'Winter':
        car_type = 'Jeep'
        car_cost = budget * 0.80

elif budget > 500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    car_cost = budget * 0.90

print(f'{car_class}')
print(f'{car_type} - {car_cost:.2f}')