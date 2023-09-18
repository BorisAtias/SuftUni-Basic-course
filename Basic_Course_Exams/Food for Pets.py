days_count = int(input())
food_total_grams = float(input())

biscuits_count = 0
total_food_eaten = 0
dog_portion = 0
cat_portion = 0

for food_per_day in range(1, days_count + 1):

    eaten_by_dog = int(input())
    dog_portion += eaten_by_dog

    eaten_by_cat = int(input())
    cat_portion += eaten_by_cat

    if food_per_day % 3 == 0:
        biscuits_count += (eaten_by_cat + eaten_by_dog) * 0.10

    total_food_eaten += eaten_by_cat + eaten_by_dog

print(f"Total eaten biscuits: {round(biscuits_count)}gr.")
print(f"{(total_food_eaten / food_total_grams) * 100:.2f}% of the food has been eaten.")
print(f"{(dog_portion / total_food_eaten) * 100:.2f}% eaten from the dog.")
print(f"{(cat_portion / total_food_eaten) * 100:.2f}% eaten from the cat.")
