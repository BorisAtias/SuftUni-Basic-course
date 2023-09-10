season = str(input())
group = str(input())
students_count = int(input())
nights_count = int(input())

price_per_night = 0
total_price = 0
sport = ''

if season == "Winter":

    if group == 'boys':
        price_per_night = 9.60
        sport = 'Judo'

    elif group == 'girls':
        price_per_night = 9.60
        sport = 'Gymnastics'

    if group == "mixed":
        price_per_night = 10
        sport = 'Ski'

elif season == "Spring":

    if group == 'boys':
        price_per_night = 7.20
        sport = 'Tennis'

    elif group == 'girls':
        price_per_night = 7.20
        sport = 'Athletics'

    if group == "mixed":
        price_per_night = 9.50
        sport = 'Cycling'

elif season == "Summer":

    if group == 'boys':
        price_per_night = 15
        sport = 'Football'

    elif group == 'girls':
        price_per_night = 15
        sport = 'Volleyball'

    if group == "mixed":
        price_per_night = 20
        sport = 'Swimming'

total_price = price_per_night * nights_count * students_count


discount = 0

if students_count >= 50:
    discount = total_price * 0.50

elif 20 <= students_count < 50:
    discount = total_price * 0.15

elif 10 <= students_count < 20:
    discount = total_price * 0.05

print(f'{sport} {total_price - discount:.2f} lv.')