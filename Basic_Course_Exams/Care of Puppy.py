food_bought_kg = int(input()) * 1000

food_eaten = 0
command = 'Adopted'

while True:

    food_per_meal = input()

    if food_per_meal == 'Adopted':
        break
    else:
        food_per_meal = int(food_per_meal)
        food_eaten += food_per_meal

if food_bought_kg >= food_eaten:
    print(f'Food is enough! Leftovers: {food_bought_kg - food_eaten} grams.')
else:
    print(f'Food is not enough. You need {abs(food_bought_kg - food_eaten)} grams more.')
