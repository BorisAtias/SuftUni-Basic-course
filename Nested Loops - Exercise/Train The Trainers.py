jury_members = int(input())
presentation_title = input()

final_average_score = 0
presentation_count = 0

while presentation_title != "Finish":

    presentation_count += 1
    grades_sum = 0

    for grades in range(jury_members):
        presentation_grades = float(input())
        grades_sum += presentation_grades

    average_score = grades_sum / jury_members

    print(f'{presentation_title} - {average_score:.2f}.')

    final_average_score += average_score

    presentation_title = input()

print(f"Student's final assessment is {final_average_score / presentation_count:.2f}.")