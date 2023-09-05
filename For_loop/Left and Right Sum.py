num_1 = int(input())

sum_left = 0
sum_right = 0


for num in range(num_1):
    current_num = int(input())
    sum_left += current_num

for num in range(num_1):
    current_num = int(input())
    sum_right += current_num


if sum_left == sum_right:
    print(f'Yes, sum = {sum_left}')

else:
    diff = abs(sum_left - sum_right)
    print(f'No, diff = {diff}')
