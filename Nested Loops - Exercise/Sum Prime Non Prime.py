prime_list = []
non_prime_list = []
while True:
    num = input()
    not_prime = False

    if num == 'stop':
        break

    num = int(num)

    if num < 0:
        print("Number is negative.")
        continue
    elif num == 1:
        not_prime = True
    else:
        for i in range(2, num):
            if num % i == 0 and num != 2:
                not_prime = True
                break
        if not_prime:
            non_prime_list.append(num)
        else:
            prime_list.append(num)


print(f'Sum of all prime numbers is: {sum(prime_list)}')
print(f'Sum of all non prime numbers is: {sum(non_prime_list)}')




