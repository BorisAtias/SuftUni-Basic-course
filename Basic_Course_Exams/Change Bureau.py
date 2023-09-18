BT_count = int(input())
yuan_count = float(input())
commission = float(input())

BT_price_lv = 1168 * BT_count
yuan_price_lv = 0.15 * yuan_count * 1.76

total_Brutto_euro = (BT_price_lv + yuan_price_lv) / 1.95

total_Netto_euro = total_Brutto_euro - ((total_Brutto_euro * commission) / 100)
print(f'{total_Netto_euro:.2f}')