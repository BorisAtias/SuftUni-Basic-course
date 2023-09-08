weekends_count = int(input())

yearly_playtime_needs = 30000
play_minutes_work_days = 63
play_minutes_weekends = 127

total_work_days = 365 - weekends_count

total_playing_time = (total_work_days * play_minutes_work_days) + (weekends_count * play_minutes_weekends)
total_playtime_spent = abs(yearly_playtime_needs - total_playing_time)

playing_minutes = total_playtime_spent % 60
playing_hours = (total_playtime_spent - playing_minutes) / 60

if total_playing_time > yearly_playtime_needs:
    print('Tom will run away')
    print(f'{int(abs(playing_hours))} hours and {playing_minutes} minutes more for play')
elif total_playing_time < yearly_playtime_needs:
    print('Tom sleeps well')
    print(f'{int(abs(playing_hours))} hours and {playing_minutes} minutes less for play')