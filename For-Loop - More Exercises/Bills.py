period = int(input())

electricity = 0
water = 20 * period
internet = 15 * period


for bill in range(1, period + 1):
    electro_bill_month = float(input())

    electricity += electro_bill_month

others = (water + internet + electricity) + (water + internet + electricity) * 0.20

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {(electricity + water + internet + others) / period:.2f} lv')

