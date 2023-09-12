needed_sum = float(input())
available_money = float(input())

days_counter = 0
spend_count = 0


while available_money < needed_sum and spend_count < 5:
    spend_or_save = input()
    money = float(input())

    days_counter += 1

    if spend_or_save == "save":
        available_money += money
        spend_count = 0

    elif spend_or_save == 'spend':
        spend_count += 1
        available_money -= money

        if available_money < 0:
            available_money = 0

if spend_count == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")
else:
    print(f'You saved the money for {days_counter} days.')