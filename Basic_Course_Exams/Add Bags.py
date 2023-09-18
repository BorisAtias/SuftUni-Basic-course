over_20_kg_price = float(input())
luggage_weight = float(input())
days_before_flight = int(input())
luggage_count = int(input())

price_up_to_10_kg = over_20_kg_price * 0.20
price_btw_10_20 = over_20_kg_price * 0.50

total_bill = 0

if luggage_weight > 20:
    total_bill = over_20_kg_price * luggage_count

if 10 <= luggage_weight <= 20:
    total_bill = price_btw_10_20 * luggage_count

if luggage_weight < 10:
    total_bill = price_up_to_10_kg * luggage_count

if days_before_flight < 7:
    total_bill = total_bill + total_bill * 0.40
elif 7 <= days_before_flight <= 30:
    total_bill = total_bill + total_bill * 0.15
elif days_before_flight > 30:
    total_bill = total_bill + total_bill * 0.10


print(f" The total price of bags is: {total_bill:.2f} lv. ")