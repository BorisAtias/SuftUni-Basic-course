total_students_num = int(input())

failed_grades_count = 0
good_grades_count = 0
very_good_grades_count = 0
top_grades_count = 0

total_grades_sum = 0

for grades in range(1, total_students_num + 1):
    student_grade = float(input())

    if student_grade < 3.00:
        failed_grades_count += 1
        total_grades_sum += student_grade

    elif 3.00 <= student_grade <= 3.99:
        good_grades_count += 1
        total_grades_sum += student_grade

    elif 4.00 <= student_grade <= 4.99:
        very_good_grades_count += 1
        total_grades_sum += student_grade
    else:
        top_grades_count += 1
        total_grades_sum += student_grade

print(f'Top students: {(top_grades_count / total_students_num) * 100:.2f}%')
print(f'Between 4.00 and 4.99: {(very_good_grades_count / total_students_num) * 100:.2f}%')
print(f'Between 3.00 and 3.99: {(good_grades_count / total_students_num) * 100:.2f}%')
print(f'Fail: {(failed_grades_count / total_students_num) * 100:.2f}%')
print(f'Average: {total_grades_sum / total_students_num:.2f}')