order_count = int(input())
order_type = input()
delivery_choice = input()

bill = 0

if order_count < 10:
    print('Invalid order')

else:
    if order_type == '90X130':
        bill += order_count * 110
        if 30 < order_count <= 60:
            bill -= bill * 0.05
        elif order_count > 60:
            bill -= bill * 0.08

    elif order_type == '100X150':
        bill += order_count * 140
        if 40 < order_count <= 80:
            bill -= bill * 0.06
        elif order_count > 80:
            bill -= bill * 0.10

    elif order_type == '130X180':
        bill += order_count * 190
        if 20 < order_count <= 50:
            bill -= bill * 0.07
        elif order_count > 50:
            bill -= bill * 0.12

    elif order_type == '200X300':
        bill += order_count * 250
        if 25 < order_count <= 50:
            bill -= bill * 0.09
        elif order_count > 50:
            bill -= bill * 0.14

    if delivery_choice == "With delivery":
        bill += 60
    else:
        pass
    if order_count > 99:
        bill -= bill * 0.04

    print(f'{bill:.2f} BGN')
