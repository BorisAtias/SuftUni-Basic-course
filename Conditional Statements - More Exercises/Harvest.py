from math import floor
from math import ceil

land_square_meters = int(input())
grapes_per_square_meter = float(input())
wine_needed_liter = int(input())
workers_count = int(input())

wine_parcel = land_square_meters * 0.40
grape_production = wine_parcel * grapes_per_square_meter
grape_per_wine_liter = 2.5

wine_produced = grape_production / grape_per_wine_liter

if wine_produced < wine_needed_liter:
    print(f'It will be a tough winter! More {floor(abs(wine_produced - wine_needed_liter))} liters wine needed.')
elif wine_produced >= wine_needed_liter:
    print(f'Good harvest this year! Total wine: {floor(wine_produced)} liters.')
    print(f'{ceil(abs(wine_needed_liter - wine_produced))} liters left -> {ceil(abs(wine_needed_liter - wine_produced) / workers_count)} liters per person.')