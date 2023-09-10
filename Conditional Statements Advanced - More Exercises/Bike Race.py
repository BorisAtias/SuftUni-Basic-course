junior_count = int(input())
senior_count = int(input())
race_type = str(input())

race_fund = 0

if race_type == 'trail':
    race_fund = (junior_count * 5.50) + (senior_count * 7)

elif race_type == 'cross-country':
    if junior_count + senior_count >= 50:
        race_fund = ((junior_count * 8) + (senior_count * 9.50)) - ((junior_count * 8) + (senior_count * 9.50)) * 0.25

    else:
        race_fund = (junior_count * 8) + (senior_count * 9.5)

elif race_type == 'downhill':
    race_fund = (junior_count * 12.25) + (senior_count * 13.75)

elif race_type == 'road':
    race_fund = (junior_count * 20) + (senior_count * 21.50)


giveaway_fund = race_fund - (race_fund * 0.05)
print(f'{giveaway_fund:.2f}')