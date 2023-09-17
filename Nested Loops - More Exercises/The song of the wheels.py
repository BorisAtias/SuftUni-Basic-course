num = int(input())

password = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == num:
                    if a < b and c > d:
                        password.append(f"{a}{b}{c}{d}")
print(*password)

if len(password) < 4:
    print("No!")
else:
    print(f"Password: {password[3]}")