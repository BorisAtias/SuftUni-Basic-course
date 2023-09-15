standard = 0
kid = 0
student = 0

while True:

    film_name = input()

    if film_name == 'Finish':
        break

    hall_capacity = int(input())
    sold_tickets = 0

    while sold_tickets < hall_capacity:

        ticket_types = input()

        if ticket_types == 'End':
            break

        if ticket_types == 'standard':
            standard += 1
        elif ticket_types == 'kid':
            kid += 1
        elif ticket_types == 'student':
            student += 1
        sold_tickets += 1

    print(f"{film_name} - {(sold_tickets / hall_capacity) * 100:.2f}% full.")

total_tickets_sold = standard + kid + student

print(f"Total tickets: {total_tickets_sold}")
print(f"{student / total_tickets_sold * 100:.2f}% student tickets.")
print(f"{standard / total_tickets_sold * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets_sold * 100:.2f}% kids tickets.")