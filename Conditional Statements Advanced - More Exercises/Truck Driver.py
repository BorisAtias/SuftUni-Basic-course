season = str(input())
km_per_month = float(input())

complete_season = km_per_month * 4
income_per_km = 0

if season == 'Spring' or season == "Autumn":

    if km_per_month <= 5000:
        income_per_km = 0.75

    elif 5000 < km_per_month <= 10000:
        income_per_km = 0.95

    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45

elif season == 'Summer':

    if km_per_month <= 5000:
        income_per_km = 0.90

    elif 5000 < km_per_month <= 10000:
        income_per_km = 1.10

    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45

elif season == 'Winter':

    if km_per_month <= 5000:
        income_per_km = 1.05

    elif 5000 < km_per_month <= 10000:
        income_per_km = 1.25

    elif 10000 < km_per_month <= 20000:
        income_per_km = 1.45

season_income_brutto = (km_per_month * income_per_km) * 4

tax = season_income_brutto * 0.10

season_income_Netto = season_income_brutto - tax

print(f'{season_income_Netto:.2f}')