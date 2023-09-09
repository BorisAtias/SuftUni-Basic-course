actor = input()
academy_points = float(input())
jury_count = int(input())

actor_score = 0
result = 0

nominee_points_needed = 1250.5


for i in range(0, jury_count):
    jury_member = input()
    jury_member_score = float(input())

    length_of_name = len(jury_member)
    actor_score += (length_of_name * jury_member_score) / 2
    result = academy_points + actor_score
    final_result = abs(1250.5 - result)

    if result >= 1250.50:
        break

if result >= nominee_points_needed:
    print(f"Congratulations, {actor} got a nominee for leading role with {result:.1f}!")

elif result < nominee_points_needed:
    print(f"Sorry, {actor} you need {abs(1250.5 - result):.1f} more!")