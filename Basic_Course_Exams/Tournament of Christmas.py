tournament_duration = int(input())

win_count = 0

daily_win_count = 0

money_won_daily = 0
money_won_total = 0

command = 'Finish'
for days_count in range(1, tournament_duration + 1):
    while True:

        sport = input()
        if sport == 'Finish':
            if daily_win_count > 0:
                money_won_total += money_won_daily + money_won_daily * 0.10
            else:
                money_won_total += money_won_daily
            daily_win_count = 0
            daily_lost_count = 0
            money_won_daily = 0
            break
        else:
            outcome = input()
            if outcome == 'win':
                daily_win_count += 1
                win_count += 1
                money_won_daily += 20
            else:
                daily_win_count -= 1
                win_count -= 1


if win_count > 0:
    money_won_total += money_won_total * 0.20
    print(f"You won the tournament! Total raised money: {money_won_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_won_total:.2f}")
