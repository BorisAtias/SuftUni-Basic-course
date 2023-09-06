num = int(input())
result = 0

while num >= result:
    num1 = int(input())

    result += num1
    if result >= num:
        break

    else:
        continue

print(result)