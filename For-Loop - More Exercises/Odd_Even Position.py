n = int(input())

main_list = []
odd_num = []
even_num = []
no = "No"

for i in range(1, n + 1):
    num = float(input())
    main_list.append(num)
    odd_num.append(main_list[0::2])
    even_num.append(main_list[1::2])

if n <= 0:
    num = 0
    print(f'OddSum={num:.2f},')
    print(f'OddMin={no},')
    print(f'OddMax={no},')
    print(f'EvenSum={num:.2f},')
    print(f'EvenMin={no},')
    print(f'EvenMax={no} ')

if n > 0:
    print(f'OddSum={sum(odd_num[n - 1]):.2f},')
    print(f'OddMin={min(odd_num[n - 1]):.2f},')
    print(f'OddMax={max(odd_num[n - 1]):.2f},')

if 0 < n <= 1:
    print(f'EvenSum={sum(even_num[n - 1]):.2f},')
    print(f'EvenMin={no},')
    print(f'EvenMax={no}')

if n > 1:
    print(f'EvenSum={sum(even_num[n - 1]):.2f},')
    print(f'EvenMin={min(even_num[n - 1]):.2f},')
    print(f'EvenMax={max(even_num[n - 1]):.2f} ')
