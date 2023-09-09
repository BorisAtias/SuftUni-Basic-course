from math import floor

tournament_count = int(input())
starting_points = int(input())

w_points = 0
w_count = 0
f_points = 0
sf_points = 0

for i in range(tournament_count):
    tournament_progress = input()

    if tournament_progress == 'W':
        w_count += 1
        w_points += 2000

    elif tournament_progress == 'F':
        f_points += 1200

    elif tournament_progress == 'SF':
        sf_points += 720

final_points = w_points + f_points + sf_points + starting_points
average_points = (w_points + f_points + sf_points) / tournament_count
percent_wins = (w_count / tournament_count) * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percent_wins:.2f}%')