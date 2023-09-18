from math import floor

current_record_sec = float(input())
distance_meters = float(input())
sec_per_meter = float(input())

new_time = distance_meters * sec_per_meter
delay = floor(distance_meters / 50) * 30

if new_time + delay < current_record_sec:
    print(f" Yes! The new record is {new_time + delay:.2f} seconds.")
else:
    print(f"No! He was {abs(current_record_sec - (new_time + delay)):.2f} seconds slower.")