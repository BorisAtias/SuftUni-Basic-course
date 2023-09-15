num_1 = int(input())
num_2 = int(input())

for number in range(num_1, num_2 + 1):
    number_to_string = str(number)

    sum_even = 0
    sum_odd = 0

    for index, digit in enumerate(number_to_string):

        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(number, end=' ')