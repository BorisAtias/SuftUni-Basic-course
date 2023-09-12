bottles_detergent = int(input()) * 750

dishes_count = 0
dishes_consume = 5

pots_count = 0
pots_consume = 15

dishwasher_fills = 0


while bottles_detergent >= 0:

    dirty_stuff = input()

    if dirty_stuff == 'End':
        break

    dirty_stuff = int(dirty_stuff)

    dishwasher_fills += 1

    if dishwasher_fills % 3 == 0:
        pots_count += dirty_stuff
        bottles_detergent -= dirty_stuff * pots_consume

    else:
        dishes_count += dirty_stuff
        bottles_detergent -= dirty_stuff * dishes_consume

if bottles_detergent >= 0:
    print(f'Detergent was enough!')
    print(f'{dishes_count} dishes and {pots_count} pots were washed.')
    print(f'Leftover detergent {bottles_detergent} ml.')
else:
    print(f'Not enough detergent, {abs(bottles_detergent)} ml. more necessary!')