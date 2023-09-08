fuel_type = str(input())
fuel_volume = float(input())
club_card = str(input())

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_club_discount = gasoline_price - 0.18
diesel_club_discount = diesel_price - 0.12
gas_club_discount = gas_price - 0.08

bill_total = 0

if fuel_type == 'Gasoline' and club_card == 'Yes':
    if fuel_volume < 20:
        bill_total = gasoline_club_discount * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (gasoline_club_discount * fuel_volume) - (gasoline_club_discount * fuel_volume) * 0.08
    elif fuel_volume > 25:
        bill_total = (gasoline_club_discount * fuel_volume) - (gasoline_club_discount * fuel_volume) * 0.10

if fuel_type == 'Gasoline' and club_card == 'No':
    if fuel_volume < 20:
        bill_total = gasoline_price * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (gasoline_price * fuel_volume) - (gasoline_price * fuel_volume) * 0.08
    elif fuel_volume > 25:
        bill_total = (gasoline_price * fuel_volume) - (gasoline_price * fuel_volume) * 0.10


if fuel_type == 'Diesel' and club_card == 'Yes':
    if fuel_volume < 20:
        bill_total = diesel_club_discount * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (diesel_club_discount * fuel_volume) - (diesel_club_discount * fuel_volume) * 0.08
    elif fuel_volume > 25:
        bill_total = (diesel_club_discount * fuel_volume) - (diesel_club_discount * fuel_volume) * 0.10

if fuel_type == 'Diesel' and club_card == 'No':
    if fuel_volume < 20:
        bill_total = diesel_price * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (diesel_price * fuel_volume) - (diesel_price * fuel_volume) * 0.08
    elif fuel_volume > 25:
        bill_total = (diesel_price * fuel_volume) - (diesel_price * fuel_volume) * 0.10


if fuel_type == 'Gas' and club_card == 'Yes':
    if fuel_volume < 20:
        bill_total = gas_club_discount * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (gas_club_discount * fuel_volume) - (gas_club_discount * fuel_volume) * 0.08
    elif fuel_volume > 25:
        bill_total = (gas_club_discount * fuel_volume) - (gas_club_discount * fuel_volume) * 0.10

if fuel_type == 'Gas' and club_card == 'No':
    if fuel_volume < 20:
        bill_total = gas_price * fuel_volume
    elif 20 <= fuel_volume <= 25:
        bill_total = (gas_price * fuel_volume) - ((gas_price * fuel_volume) * 0.08)
    elif fuel_volume > 25:
        bill_total = (gas_price * fuel_volume) - ((gas_price * fuel_volume) * 0.10)

print(f'{bill_total:.2f} lv.')