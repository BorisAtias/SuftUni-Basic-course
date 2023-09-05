num_1 = int(input())

sum_even = 0
sum_odd = 0


for num in range(1, num_1 + 1):
    current_num = int(input())
    if num % 2 == 0:
        sum_even += current_num
    else:
        sum_odd += current_num

if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')
else:
    diff = abs(sum_even - sum_odd)
    print('No')
    print(f'Diff = {diff}')
