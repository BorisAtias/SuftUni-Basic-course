from math import floor
ball_count = int(input())

red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
others_count = 0

total_points = 0

for points in range(ball_count):

    colors = input()

    if colors == 'red':
        red_count += 1
        total_points += 5
    elif colors == 'orange':
        orange_count += 1
        total_points += 10
    elif colors == 'yellow':
        yellow_count += 1
        total_points += 15
    elif colors == 'white':
        white_count += 1
        total_points += 20
    elif colors == 'black':
        black_count += 1
        total_points = floor(total_points / 2)
    else:
        others_count += 1
        continue
print(f'Total points: {total_points}')
print(f'Red balls: {red_count}')
print(f'Orange balls: {orange_count}')
print(f'Yellow balls: {yellow_count}')
print(f'White balls: {white_count}')
print(f'Other colors picked: {others_count}')
print(f'Divides from black balls: {black_count}')
