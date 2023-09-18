taste = input()
set_size = input()
sets_ordered = int(input())

price = 0
set_small = 2
set_big = 5
if taste == 'Watermelon':
    if set_size == 'small':
        price += (set_small * 56) * sets_ordered
    else:
        price += (set_big * 28.70) * sets_ordered

elif taste == 'Mango':
    if set_size == 'small':
        price += (set_small * 36.66) * sets_ordered
    else:
        price += (set_big * 19.60) * sets_ordered

elif taste == 'Pineapple':
    if set_size == 'small':
        price += (set_small * 42.10) * sets_ordered
    else:
        price += (set_big * 24.80) * sets_ordered

elif taste == 'Raspberry':
    if set_size == 'small':
        price += (set_small * 20) * sets_ordered
    else:
        price += (set_big * 15.20) * sets_ordered

if 400 <= price <= 1000:
    price -= price * 0.15
elif price > 1000:
    price -= price * 0.50

print(f"{price:.2f} lv.")