walking_time_min = int(input())
walks_count = int(input())
calories_intake = int(input())

calories_spent_min = 5

if (walking_time_min * walks_count) * 5 >= calories_intake / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {(walking_time_min * walks_count) * 5}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {(walking_time_min * walks_count) * 5}.")