interval_begin = int(input())
interval_end = int(input())

magic_number = int(input())

combinations_count = 0

comb_found = False

for i in range(interval_begin, interval_end + 1):
    for j in range(interval_begin, interval_end + 1):

        combinations_count += 1

        if i + j == magic_number:
            print(f"Combination N:{combinations_count} ({i} + {j} = {magic_number})")
            comb_found = True
            break

    if comb_found:
        break

if not comb_found:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
