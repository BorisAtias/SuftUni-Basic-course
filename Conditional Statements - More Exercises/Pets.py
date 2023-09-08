from math import floor
from math import ceil

day_count = int(input())
food_provided_kg = int(input())
daily_food_dog_kg = float(input())
daily_food_cat_kg = float(input())
daily_food_turtle_gram = float(input())

total_food_for_all = ((daily_food_dog_kg  + daily_food_cat_kg) +(daily_food_turtle_gram / 1000)) * day_count

if total_food_for_all <= food_provided_kg:
    print(f'{floor(food_provided_kg - total_food_for_all)} kilos of food left.')
elif total_food_for_all > food_provided_kg:
    print(f'{ceil(abs(total_food_for_all - food_provided_kg))} more kilos of food are needed.')