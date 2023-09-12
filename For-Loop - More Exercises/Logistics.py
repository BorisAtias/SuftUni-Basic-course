total_orders = int(input())

total_price_bus = 0
bus_total_tons = 0

total_price_truc = 0
truck_total_tons = 0

total_price_train = 0
train_total_tons = 0

total_tons_count = 0

for load in range(1, total_orders + 1):
    load_weight_tons = int(input())

    if load_weight_tons <= 3:
        bus_total_tons += load_weight_tons
        total_tons_count += load_weight_tons
        total_price_bus += load_weight_tons * 200

    elif 4 <= load_weight_tons <= 11:
        truck_total_tons += load_weight_tons
        total_tons_count += load_weight_tons
        total_price_truc += load_weight_tons * 175

    elif load_weight_tons >= 12:
        train_total_tons += load_weight_tons
        total_tons_count += load_weight_tons
        total_price_train += load_weight_tons * 120

average_price_per_ton = (total_price_bus + total_price_truc + total_price_train) / total_tons_count

print(f'{average_price_per_ton:.2f}')
print(f'{(bus_total_tons / total_tons_count) * 100:.2f}%')
print(f'{(truck_total_tons / total_tons_count) * 100:.2f}%')
print(f'{(train_total_tons / total_tons_count) * 100:.2f}%')