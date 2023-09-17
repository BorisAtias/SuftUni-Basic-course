days = int(input())
hours_per_day = int(input())

day_count = 0
hour_count = 0
current_price = 0
price = 0

for day in range(1, days + 1):
    for hours in range(1, hours_per_day + 1):

        if day % 2 == 0 and hours % 2 != 0:
            current_price += 2.50

        elif day % 2 != 0 and hours % 2 == 0:
            current_price += 1.25

        else:
            current_price += 1

    print(f'Day: {day} - {current_price:.2f} leva')
    price += current_price
    current_price = 0

print(f'Total: {price:.2f} leva')
