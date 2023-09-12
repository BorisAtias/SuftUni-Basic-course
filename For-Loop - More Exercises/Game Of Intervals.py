num_game_moves = int(input())

zero_to_nine_count = 0
ten_to_nineteen_count = 0
twenty_to_twentynine_count = 0
thirty_to_thirtynine_count = 0
forty_to_fifty_count = 0
invalid_num_count = 0

result = 0

for points in range(1, num_game_moves + 1):
    new_nums = int(input())

    if 0 <= new_nums <= 9:
        zero_to_nine_count += 1
        result += (new_nums * 20) / 100

    elif 10 <= new_nums <= 19:
        ten_to_nineteen_count += 1
        result += (new_nums * 30) / 100

    elif 20 <= new_nums <= 29:
        twenty_to_twentynine_count += 1
        result += (new_nums * 40) / 100

    elif 30 <= new_nums <= 39:
        thirty_to_thirtynine_count += 1
        result += 50

    elif 40 <= new_nums <= 50:
        forty_to_fifty_count += 1
        result += 100

    else:
        invalid_num_count += 1
        result -= result / 2

print(f'{result:.2f}')
print(f'From 0 to 9: {(zero_to_nine_count / num_game_moves) * 100:.2f}%')
print(f'From 10 to 19: {(ten_to_nineteen_count / num_game_moves) * 100:.2f}%')
print(f'From 20 to 29: {(twenty_to_twentynine_count / num_game_moves) * 100:.2f}%')
print(f'From 30 to 39: {(thirty_to_thirtynine_count / num_game_moves) * 100:.2f}%')
print(f'From 40 to 50: {(forty_to_fifty_count / num_game_moves) * 100:.2f}%')
print(f'Invalid numbers: {(invalid_num_count / num_game_moves) * 100:.2f}%')
