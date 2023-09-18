needed_profit = float(input())
total_income = 0
command = 'Party'

while True:

    coctail_name = input()

    if coctail_name == 'Party!':
        break
    else:
        coctale_ordered = int(input())

        order_price = coctale_ordered * len(coctail_name)

        if order_price % 2 != 0:
            order_price -= order_price * 0.25


        total_income += order_price
    if total_income >= needed_profit:
        break


if total_income >= needed_profit:
    print(f'Target acquired.')
else:
    print(f'We need {needed_profit - total_income:.2f} leva more.')

print(f'Club income - {total_income:.2f} leva.')
