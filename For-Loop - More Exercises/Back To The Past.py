heritage = float(input())
year_to_live_to = int(input())

current_age = 18

even_year_expense = 12000

for year_to_live_in in range(1800, year_to_live_to + 1):
    if year_to_live_in % 2 == 0:
        heritage -= even_year_expense
        current_age += 1

        if year_to_live_in > year_to_live_to:
            break

    else:
        heritage -= even_year_expense + 50 * current_age
        current_age += 1

        if year_to_live_in > year_to_live_to:
            break


if heritage >= 0:
    print(f'Yes! He will live a carefree life and will have {heritage:.2f} dollars left.')
else:
    print(f'He will need {abs(heritage):.2f} dollars to survive.')