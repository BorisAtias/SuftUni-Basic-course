hall_rent = float(input())

cake = hall_rent * 0.20
drinks = cake - (cake * 0.45)
animator = hall_rent / 3

budget = hall_rent + cake + drinks + animator
print(budget)
