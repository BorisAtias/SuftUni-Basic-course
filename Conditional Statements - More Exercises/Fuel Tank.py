diesel_gasoline_gas = str(input())
liters_in_reservoir = float(input())


if diesel_gasoline_gas == 'Diesel':
    if liters_in_reservoir >= 25:
        print(f'You have enough {(diesel_gasoline_gas.lower())}.')
    elif liters_in_reservoir < 25:
        print(f'Fill your tank with {(diesel_gasoline_gas.lower())}!')


elif diesel_gasoline_gas == 'Gasoline':
    if liters_in_reservoir >= 25:
        print(f'You have enough {(diesel_gasoline_gas.lower())}.')
    elif liters_in_reservoir < 25:
        print(f'Fill your tank with {(diesel_gasoline_gas.lower())}!')


elif diesel_gasoline_gas == 'Gas':
    if liters_in_reservoir >= 25:
        print(f'You have enough {(diesel_gasoline_gas.lower())}.')
    elif liters_in_reservoir < 25:
        print(f'Fill your tank with {(diesel_gasoline_gas.lower())}!')

else:
    print("Invalid fuel!")