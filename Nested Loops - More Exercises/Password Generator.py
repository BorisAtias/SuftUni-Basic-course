n = int(input())
l = int(input())

passwords = []

for symbol1 in range(1, n + 1):
    for symbol2 in range(1, n + 1):
        for symbol3 in range(97, (97 + l)):
            for symbol4 in range(97, (97 + l)):
                for symbol5 in range(1, n + 1):
                    if symbol5 > symbol1 and symbol5 > symbol2:
                        passwords.append(f'{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}')

print(*passwords, sep=" ")