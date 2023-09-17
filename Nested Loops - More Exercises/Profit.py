coins_1_lv = int(input())
coins_2_lv = int(input())
bills_5_lv = int(input())
total_amount = int(input())

for i in range(coins_1_lv + 1):
    for j in range(coins_2_lv + 1):
        for x in range(bills_5_lv + 1):

            if (i * 1) + (j * 2) + (x * 5) == total_amount:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {x} * 5 lv. = {total_amount} lv.')
