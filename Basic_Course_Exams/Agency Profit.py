company = input()
full_prise_tickets_count = int(input())
kids_tickets_count = int(input())
nett_ticket_price = float(input())
service_tax = float(input())

full_ticket_price = nett_ticket_price + service_tax
kids_tickets_price = nett_ticket_price - nett_ticket_price * 0.70 + service_tax

brutto_profit = (full_prise_tickets_count * full_ticket_price) + (kids_tickets_price * kids_tickets_count)
nett_profit = brutto_profit * 0.20

print(f"The profit of your agency from {company} tickets is {nett_profit:.2f} lv.")
