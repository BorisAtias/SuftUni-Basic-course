mackerel_price = float(input())
sprat_fish_price = float(input())
bonito_fish_kg = float(input())
scad_fish_kg = float(input())
oysters_kg = int(input())

bonito_fish_price_kg = (mackerel_price + (mackerel_price * 0.60)) * bonito_fish_kg
scad_fish_price = (sprat_fish_price + (sprat_fish_price * 0.80)) * scad_fish_kg
oysters_price = oysters_kg * 7.50

bill = bonito_fish_price_kg + scad_fish_price + oysters_price

print(f'{bill:.2f}')