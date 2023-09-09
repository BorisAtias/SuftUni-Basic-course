age = int(input())
wash_machine = float(input())
toy_price = int(input())

birthday_gift_even = 0

piggy_bank = 0
toy_count = 0

brother_deduction = 0


for aging in range(1, age + 1):
    if aging % 2 != 0:
        toy_count += 1

    else:
        birthday_gift_even += 1
        brother_deduction += 1

        if aging != 2:
            piggy_bank += 10 * birthday_gift_even

        else:
            piggy_bank += 10

total_savings = (toy_count * toy_price) + piggy_bank - brother_deduction

if total_savings >= wash_machine:
    print(f'Yes! {total_savings - wash_machine:.2f}')

else:
    print(f'No! {abs(total_savings - wash_machine):.2f}')