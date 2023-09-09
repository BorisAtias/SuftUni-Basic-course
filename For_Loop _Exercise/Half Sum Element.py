n = int(input())

max_num = []
sum_num = 0

for i in range(1, n + 1):
    num = int(input())
    max_num.append(num)
    sum_num += num

highest_value = int(max(max_num))
diff_nums = int(sum_num - highest_value)

if diff_nums == highest_value:
    print('Yes')
    print(f'Sum = {highest_value}')
else:
    print('No')
    diff_sum = highest_value - diff_nums
    print(f'Diff = {abs(diff_sum)}')