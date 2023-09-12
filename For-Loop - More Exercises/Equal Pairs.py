num_1 = int(input())
sum = int(input()) + int(input())

maxdiff = 0

for i in range(num_1 - 1):
    current_sum = int(input()) + int(input())

    if abs(sum - current_sum) > maxdiff:
         maxdiff = abs(sum - current_sum)

    sum = current_sum

if maxdiff == 0:
    print(f'Yes, value={sum}')
else:
    print(f' No, maxdiff={maxdiff}')