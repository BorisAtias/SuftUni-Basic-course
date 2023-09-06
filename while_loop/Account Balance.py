total = 0

while True:

    income = input()
    if income == 'NoMoreMoney':
        print(f'Total: {total:.2f}')
        break

    income = float(income)
    total += income

    if income >= 0:
        print(f"Increase: {income:.2f}")

    elif income < 0:
        print("Invalid operation!")
        print(f'Total: {total - income:.2f}')
        break

    else:
        continue