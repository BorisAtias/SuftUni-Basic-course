room_w_cm = float(input()) * 100
room_h_cm = float(input()) * 100 - 100

working_spots_w = (room_w_cm / 120)
working_spots_h = (room_h_cm / 70)

total_working_spots = int(working_spots_h) * int(working_spots_w) - 3

print(f'{total_working_spots}')