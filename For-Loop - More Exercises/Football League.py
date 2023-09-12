stadium_capacity = int(input())
total_fans = int(input())

sector_A_count = 0
sector_B_count = 0
sector_V_count = 0
sector_G_count = 0

for i in range(1, total_fans + 1):
    sector = str(input())

    if sector == 'A':
        sector_A_count += 1

    elif sector == 'B':
        sector_B_count += 1

    elif sector == 'V':
        sector_V_count += 1

    elif sector == 'G':
        sector_G_count += 1

print(f'{(sector_A_count / total_fans) * 100:.2f}%')
print(f'{(sector_B_count / total_fans) * 100:.2f}%')
print(f'{(sector_V_count / total_fans) * 100:.2f}%')
print(f'{(sector_G_count / total_fans) * 100:.2f}%')
print(f'{(total_fans / stadium_capacity) * 100:.2f}%')

