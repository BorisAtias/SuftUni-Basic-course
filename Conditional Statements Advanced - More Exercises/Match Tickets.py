budget = float(input())
ticket_category = str(input())
people_count = int(input())

VIP = 499.99
NORMAL = 249.99

trans_expense = 0
ticket_expense = 0

if ticket_category == 'VIP':
    ticket_expense = people_count * VIP

elif ticket_category == 'Normal':
    ticket_expense = people_count * NORMAL


if 0 < people_count <= 4:
    trans_expense = budget * 0.75

elif 5 <= people_count <= 9:
    trans_expense = budget * 0.60

elif 10 <= people_count <= 24:
    trans_expense = budget * 0.50

elif 25 <= people_count <= 49:
    trans_expense = budget * 0.40

elif people_count >= 50:
    trans_expense = budget * 0.25


ticket_budget = budget - trans_expense

leftover_money = ticket_budget - ticket_expense


if ticket_budget >= ticket_expense:
    print(f'Yes! You have {leftover_money:.2f} leva left.')

elif ticket_budget < ticket_expense:
    print(f'Not enough money! You need {abs(leftover_money):.2f} leva.')