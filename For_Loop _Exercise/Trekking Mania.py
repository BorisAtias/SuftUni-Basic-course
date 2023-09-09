groups_count = int(input())

mountain_climb = ''

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for people in range(groups_count):
    people_per_group = int(input())

    if people_per_group <= 5:
        mountain_climb = 'Musala'
        musala += people_per_group

    elif 6 <= people_per_group <= 12:
        mountain_climb = 'Monblan'
        monblan += people_per_group

    elif 13 <= people_per_group <= 25:
        mountain_climb = 'Kilimandjaro'
        kilimanjaro += people_per_group

    elif 26 <= people_per_group <= 40:
        mountain_climb = 'K2'
        k2 += people_per_group

    elif people_per_group > 40:
        mountain_climb = 'Everest'
        everest += people_per_group

total_people_count = musala + monblan + kilimanjaro + k2 + everest

print(f'{(musala / total_people_count) * 100:.2f}%')
print(f'{(monblan / total_people_count) * 100:.2f}%')
print(f'{(kilimanjaro / total_people_count) * 100:.2f}%')
print(f'{(k2 / total_people_count) * 100:.2f}%')
print(f'{(everest / total_people_count) * 100:.2f}%')