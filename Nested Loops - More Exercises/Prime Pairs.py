start_first_pair = int(input())
start_second_pair = int(input())
end_first_pair = int(input())
end_second_pair = int(input())

prime_pairs = []

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


for a in range(start_first_pair, start_first_pair + end_first_pair + 1):
    for b in range(start_second_pair, start_second_pair + end_second_pair + 1):
        if a > 9 and b > 9 and is_prime(a) and is_prime(b):
            prime_pairs.append(f"{a}{b}")

print(*prime_pairs, sep="\n")
