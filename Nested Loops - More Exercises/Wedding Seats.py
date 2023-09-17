end_sector = input()
row_count_first_sector = int(input())
odd_row_seat_count = int(input())
c = 0
for sector in range(ord("A"), ord(end_sector) + 1):
    if sector > ord("A"):
        row_count_first_sector += 1
    for rows in range(1, row_count_first_sector + 1):
        if rows % 2 == 0:
            odd_row_seat_count += 2
        for seats in range(97, (97 + odd_row_seat_count)):
            print(f"{chr(sector)}{rows}{chr(seats)}")
            c += 1
        if rows % 2 == 0:
            odd_row_seat_count -= 2

print(c)