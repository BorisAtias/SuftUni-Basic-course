n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for x in range(1, 10):
            for y in range(1, 10):

                if i + j == x + y and n % (i + j) == 0:

                    print(f'{i}{j}{x}{y}', end=' ')
