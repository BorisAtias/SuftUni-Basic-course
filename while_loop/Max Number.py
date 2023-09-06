highest_num = []

while True:
    command = input()

    if command == 'Stop':
        break

    command = int(command)
    highest_num.append(command)

print(f'{max(highest_num)}')

