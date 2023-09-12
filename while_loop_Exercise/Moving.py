available_space = int(input()) * int(input()) * int(input())

taken_space = 0

while available_space > taken_space:

    boxes = input()

    if boxes == "Done":
        break

    taken_space += int(boxes)


if available_space < taken_space:
    print(f'No more free space! You need {abs(available_space - taken_space)} Cubic meters more.')
else:
    print(f'{available_space - taken_space} Cubic meters left.')