n = float(input())

total = 0

for i in range(1, int(n + 1)):
    n_1 = int(input())

    total += n_1

print(f'{total / n:.2f}')