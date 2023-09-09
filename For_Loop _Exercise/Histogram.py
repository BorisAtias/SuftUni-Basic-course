n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for count in range(n):
    p_num = int(input())

    if p_num < 200:
        p1 += 1
    elif 200 <= p_num <= 399:
        p2 += 1
    elif 400 <= p_num <= 599:
        p3 += 1
    elif 600 <= p_num <= 799:
        p4 += 1
    elif p_num >= 800:
        p5 += 1

total_count = p1 + p2 + p3 + p4 + p5
print(f'{(p1 / total_count) * 100:.2f}%')
print(f'{(p2 / total_count) * 100:.2f}%')
print(f'{(p3 / total_count) * 100:.2f}%')
print(f'{(p4 / total_count) * 100:.2f}%')
print(f'{(p5 / total_count) * 100:.2f}%')