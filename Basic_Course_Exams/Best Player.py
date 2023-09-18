import sys

max_goal = - sys.maxsize
player_name = ''
best_player = ''
hat_trick_count = False

player = input()

while player != 'END':

    goals = int(input())
    player_name = player

    if goals > max_goal:
        max_goal = goals
        best_player = player_name
    if goals >= 10:
        break
    player = input()

print(f'{best_player} is the best player!')

if max_goal >= 3:
    print(f'He has scored {max_goal} goals and made a hat-trick !!!')
elif max_goal < 3:
    print(f'He has scored {max_goal} goals.')
