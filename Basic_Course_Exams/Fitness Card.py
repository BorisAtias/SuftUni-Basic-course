budget = float(input())
gender = input()
age = int(input())
sport = input()
price = 0

if sport == 'Gym':
    if gender == 'm':
        price += 42
    else:
        price += 35
elif sport == 'Boxing':
    if gender == 'm':
        price += 41
    else:
        price += 37
elif sport == 'Yoga':
    if gender == 'm':
        price += 45
    else:
        price += 42
elif sport == 'Zumba':
    if gender == 'm':
        price += 34
    else:
        price += 31
elif sport == 'Dances':
    if gender == 'm':
        price += 51
    else:
        price += 53
elif sport == 'Pilates':
    if gender == 'm':
        price += 39
    else:
        price += 37

if age <= 19:
    price -= price * 0.20

if price <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(price - budget):.2f} more.")