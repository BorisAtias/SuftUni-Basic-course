from math import floor
from math import ceil

magnolias_count = int(input())
zumbyuls_count = int(input())
roses_count = int(input())
cactus_count = int(input())
present_price = float(input())

magnolias = magnolias_count * 3.25
zumbyuls = zumbyuls_count * 4
roses = roses_count * 3.50
cactus = cactus_count * 8

order = magnolias + zumbyuls + roses + cactus
profit = order - (order * 0.05)

if profit >= present_price:
    print(f'She is left with {floor(profit - present_price)} leva.')
elif profit < present_price:
    print(f'She will have to borrow {ceil(abs(profit - present_price))} leva.')