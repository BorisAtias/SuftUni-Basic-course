cake = int(input()) * int(input())

eaten_pieces = 0

while cake >= eaten_pieces:

    pieces = input()

    if pieces == 'STOP':
        break

    eaten_pieces += int(pieces)

if cake < eaten_pieces:
    print(f'No more cake left! You need {abs(cake - eaten_pieces)} pieces more. ')
else:
    print(f'{cake - eaten_pieces} pieces are left.')
