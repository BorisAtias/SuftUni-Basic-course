floors = int(input())
apartments_per_floor = int(input())

apartment_type = ''
apartment_num = 0


for current_floor in range(floors, 0, - 1):
    for number in range(apartments_per_floor):

        if current_floor == floors:
            apartment_type = f'L{current_floor}{number}'

        elif current_floor % 2 == 0:
            apartment_type = f'O{current_floor}{number}'

        elif current_floor % 2 != 0:
            apartment_type = f'A{current_floor}{number}'

        print(apartment_type, end=' ')
    print()
