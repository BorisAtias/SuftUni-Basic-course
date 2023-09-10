chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = str(input())
is_it_holiday = str(input())


arrangement_price = 2

bouquet_price = 0


if season == 'Spring' or season == 'Summer':
    bouquet_price = (chrysanthemums_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)

    if season == 'Spring' and tulips_count >= 7:
        bouquet_price = bouquet_price - (bouquet_price * 0.05)


elif season == 'Autumn' or season == 'Winter':
    bouquet_price = (chrysanthemums_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)

    if season == 'Winter' and roses_count >= 10:
        bouquet_price = bouquet_price - (bouquet_price * 0.10)


if is_it_holiday == "Y":
    bouquet_price = bouquet_price + (bouquet_price * 0.15)

else:
    bouquet_price = bouquet_price


if chrysanthemums_count + roses_count + tulips_count >= 20:
    bouquet_price = bouquet_price - (bouquet_price * 0.20)

print(f'{(bouquet_price + arrangement_price):.2f}')