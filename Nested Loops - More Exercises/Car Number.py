interval_begin = int(input())
interval_end = int(input())

for i in range(interval_begin, interval_end + 1):
    for j in range(interval_begin, interval_end + 1):
        for x in range(interval_begin, interval_end + 1):
            for y in range(interval_begin, interval_end + 1):

                if i % 2 == 0 and y % 2 != 0 and (x + j) % 2 == 0 and i > y:

                    print(f'{i}{j}{x}{y}', end=' ')

                elif i % 2 != 0 and y % 2 == 0 and (x + j) % 2 == 0 and i > y:

                    print(f'{i}{j}{x}{y}', end=' ')
