num_1_end = int(input())
num_2_end = int(input())
num_3_end = int(input())


for i in range(1, num_1_end + 1):
    for j in range(2, num_2_end + 1):
        for x in range(1, num_3_end + 1):

            if i % 2 == 0 and x % 2 == 0 and j != 4 and j != 6 and j < 8:
                print(f'{i} {j} {x}')
