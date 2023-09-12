bad_grades = int(input())

fail_count = 0
solved_tasks = 0
grades_total = 0
last_task = ''

has_failed = True


while fail_count < bad_grades:

    task_name = input()
    if task_name == 'Enough':
        has_failed = False
        break

    current_grade = int(input())
    if current_grade <= 4:
        fail_count += 1
    grades_total += current_grade
    solved_tasks += 1
    last_task = task_name

if has_failed:
    print(f'You need a break, {bad_grades} poor grades.')

else:
    print(f'Average score: {grades_total / solved_tasks:.2f}')
    print(f'Number of problems: {solved_tasks}')
    print(f'Last problem: {last_task}')
