city = input()
package_type = input()
vip_status = input()
days_to_stay = int(input())


invalid_input = False
invalid_number = False

price_per_day = 0

if days_to_stay < 1:
    invalid_number = True

if days_to_stay > 7:
    days_to_stay -= 1

if city == 'Bansko' or city == 'Borovets':
    if package_type == 'withEquipment':
        price_per_day += 100
        if vip_status == 'yes':
            price_per_day -= price_per_day * 0.10
    elif package_type == 'noEquipment':
        price_per_day += 80
        if vip_status == 'yes':
            price_per_day -= price_per_day * 0.05
    else:
        invalid_input = True

elif city == 'Varna' or city == 'Burgas':
    if package_type == 'withBreakfast':
        price_per_day += 130
        if vip_status == 'yes':
            price_per_day -= price_per_day * 0.12
    elif package_type == 'noBreakfast':
        price_per_day += 100
        if vip_status == 'yes':
            price_per_day -= price_per_day * 0.07
    else:
        invalid_input = True
else:
    invalid_input = True


total_price = price_per_day * days_to_stay

if vip_status != 'yes' and vip_status != 'no':
    invalid_input = True

if invalid_number == True:
    print('Days must be positive number!')
elif invalid_input == True:
    print('Invalid input!')
else:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')