from math import ceil

people = int(input())
entry_fee = float(input())
beach_bed_price = float(input())
umbrellas_price = float(input())

entry_expense = people * entry_fee
beach_bed_expense = ceil(people * 0.75) * beach_bed_price
umbrellas_expense = ceil(people * 0.50) * umbrellas_price

total_expense = entry_expense + beach_bed_expense + umbrellas_expense

print(f'{total_expense:.2f} lv.')
