num = int(input())
sums = []

for number in range(0, num):
    new_num = int(input())
    sums.append(new_num)

print(f'Max number: {max(sums)}')
print(f'Min number: {min(sums)}')