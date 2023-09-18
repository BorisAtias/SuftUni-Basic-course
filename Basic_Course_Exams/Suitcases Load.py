trunk_capacity = float(input())

luggage_count = 0
last_luggage = 0
while trunk_capacity > 0:

    luggage = input()

    if luggage == 'End':
        print(f"Congratulations! All suitcases are loaded!")
        break
    else:
        luggage = float(luggage)

        if luggage == 0:
            continue

        if (luggage_count + 1) % 3 == 0:
            luggage *= 1.1

        if trunk_capacity < luggage:
            last_luggage += luggage
            print("No more space!")
            break

        luggage_count += 1
        trunk_capacity -= luggage

        if trunk_capacity == 0:
            print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {luggage_count} suitcases loaded.")