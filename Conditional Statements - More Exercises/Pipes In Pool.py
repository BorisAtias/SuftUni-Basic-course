pool_volume = int(input())
pipe1_per_hour = int(input())
pipe2_per_hour = int(input())
worker_absence_hours = float(input())

pipe1_total_debit = pipe1_per_hour * worker_absence_hours

pipe2_total_debit = pipe2_per_hour * worker_absence_hours


water_filled_total = pipe1_total_debit + pipe2_total_debit

pipe_1_contribution_percent = (pipe1_total_debit / water_filled_total) * 100
pipe_2_contribution_percent = (pipe2_total_debit / water_filled_total) * 100

pool_level = ((pipe1_total_debit + pipe2_total_debit) / pool_volume) * 100


if water_filled_total <= pool_volume:
    print(
        f"The pool is {pool_level:.2f}% full. Pipe 1: {pipe_1_contribution_percent:.2f}%. Pipe 2: {pipe_2_contribution_percent:.2f}%.")

if water_filled_total > pool_volume:
    print(f'For {worker_absence_hours:.2f} hours the pool overflows with {abs(pool_volume - water_filled_total):.2f} liters.')