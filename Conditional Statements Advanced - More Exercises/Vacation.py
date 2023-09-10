budget = float(input())
season = str(input())

destination = ''
accommodation = ''
vacation_cost = 0

if budget <= 1000:
    accommodation = 'Camp'

    if season == "Summer":
        destination = 'Alaska'
        vacation_cost = budget * 0.65

    elif season == 'Winter':
        destination = "Morocco"
        vacation_cost = budget * 0.45

elif 1000 < budget <= 3000:
    accommodation = 'Hut'

    if season == "Summer":
        destination = 'Alaska'
        vacation_cost = budget * 0.80

    elif season == 'Winter':
        destination = "Morocco"
        vacation_cost = budget * 0.60

elif budget > 3000:
    accommodation = 'Hotel'

    if season == "Summer":
        destination = 'Alaska'
        vacation_cost = budget * 0.90

    elif season == 'Winter':
        destination = "Morocco"
        vacation_cost = budget * 0.90

print(f'{destination} - {accommodation} - {vacation_cost:.2f}')