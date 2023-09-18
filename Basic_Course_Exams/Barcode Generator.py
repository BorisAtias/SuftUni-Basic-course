beginning = int(input())
end = int(input())

first_num = int(beginning / 1000)
second_num = int((beginning / 100) % 10)
third_num = int((beginning / 10) % 10)
forth_num = int(beginning % 10)

first_end = int(end / 1000)
second_end = int((end / 100) % 10)
third_end = int((end / 10) % 10)
forth_end = int(end % 10)
for num_1 in range(first_num, first_end + 1):
    for num_2 in range(second_num, second_end + 1):
        for num_3 in range(third_num, third_end + 1):
            for num_4 in range(forth_num, forth_end + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:

                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')
