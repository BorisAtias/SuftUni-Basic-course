veggies_prise_per_kg = float(input())
fruits_prise_per_kg = float(input())
total_veggies_kg = int(input())
total_fruits_kg = int(input())

bill = (total_veggies_kg * veggies_prise_per_kg) + (total_fruits_kg * fruits_prise_per_kg)
euro_bill = bill / 1.94
print(f'{euro_bill:.2f}')