a = int(input())
b = int(input())
max_pass_count = int(input())
A = 35
B = 64
passwords = ""

for x in range(1, a + 1):
    for y in range(1, b + 1):
        password = f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}"
        passwords += password + "|"
        A += 1
        B += 1
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        max_pass_count -= 1
        if max_pass_count == 0:
            print(passwords)
            exit()
print(passwords)



