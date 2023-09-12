needed_sum = int(input())

successful_transactions_cash = 0
cash_income_total = 0

successful_transactions_card = 0
card_income_total = 0

donations_total = 0
donation_counter = 0

while donations_total < needed_sum:

    sales = input()

    if sales == "End":
        print('Failed to collect required money for charity.')
        break

    sales = int(sales)
    donation_counter += 1

    if donation_counter % 2 != 0:

        if sales <= 100:
            successful_transactions_cash += 1
            donations_total += sales
            cash_income_total += sales
            print("Product sold!")
        else:
            print("Error in transaction!")

    if donation_counter % 2 == 0:

        if sales >= 10:
            successful_transactions_card += 1
            donations_total += sales
            card_income_total += sales
            print("Product sold!")
        else:
            print("Error in transaction!")


if donations_total >= needed_sum:
    print(f'Average CS: {cash_income_total / successful_transactions_cash:.2f}')
    print(f'Average CC: {card_income_total / successful_transactions_card:.2f}')