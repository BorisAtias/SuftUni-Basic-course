cakes = int(input())

current_points = 0
sheff_name = ''
max_points = 0
best_sheff = ''

for points in range(cakes):

    baker_name = input()
    sheff_name = baker_name

    current_points = 0

    while True:
        points_given = input()
        if points_given == 'Stop':
            print(f'{sheff_name} has {current_points} points.')
            if current_points > max_points:
                max_points = current_points
                best_sheff = sheff_name
                print(f'{best_sheff} is the new number 1!')
            break
        else:
            points_given = int(points_given)
            current_points += points_given
            continue

print(f'{best_sheff} won competition with {max_points} points!')
