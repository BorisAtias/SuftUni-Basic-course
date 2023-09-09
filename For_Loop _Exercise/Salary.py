tabs_open = int(input())
salary = float(input())

FB_penalty = 150
Insta_penalty = 100
reddit_penalty = 50

penalty_count = 0

for i in range(1, tabs_open + 1):
    web_name = input()
    if web_name == 'Facebook':
        penalty_count += 1
        salary -= FB_penalty

        if salary <= 0:
            print("You have lost your salary.")
            break
        else:
            continue

    elif web_name == "Instagram":
        penalty_count += 1
        salary -= Insta_penalty

        if salary <= 0:
            print("You have lost your salary.")
            break

        else:
            continue

    elif web_name == "Reddit":
        penalty_count += 1
        salary -= reddit_penalty

        if salary <= 0:
            print("You have lost your salary.")
            break

        else:
            continue

if salary > 0:
    print(f'{int(salary)}')