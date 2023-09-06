student_name = input()

total_grades = 0
school_years = 0
times_failed = 0

while True:

    grades = float(input())

    if grades < 4:
        times_failed += 1

        if times_failed == 2:
            print(f'{student_name} has been excluded at {school_years + 1} grade')
            break

    else:
        school_years += 1
        total_grades += grades

        if school_years == 12:
            print(f'{student_name} graduated. Average grade: {total_grades / school_years:.2f}')
            break
