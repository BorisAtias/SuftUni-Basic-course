daily_target = 10000
step_counter = 0
diff = daily_target - step_counter

while step_counter < daily_target:
    steps_walked = input()

    if steps_walked == 'Going home':
        step_counter += int(input())
        break
    steps_walked = int(steps_walked)
    step_counter += steps_walked


if step_counter >= daily_target:

    print(f'Goal reached! Good job!')
    print(f'{step_counter - daily_target} steps over the goal!')


else:
    print(f'{daily_target - step_counter} more steps to reach goal.')