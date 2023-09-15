n = int(input())


for i in range(1111, 10000):
    for digit in str(i):
        if digit == '0':
            break
        if n % int(digit) != 0:
            break
    else:
        print(i, end=' ')
