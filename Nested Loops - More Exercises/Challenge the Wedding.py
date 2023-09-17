males = int(input())
females = int(input())
tables = int(input())

while tables > 0:
    for men in range(1, males + 1):
        for woman in range(1, females + 1):
            if tables <= 0:
                break
            tables -= 1

            print(f'({men} <-> {woman}) ', end='')

    else:
        break
