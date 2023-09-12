reporting_period = int(input())

treated_patients = 0
untreated_patients = 0

doctor_count = 7

for days in range(1, reporting_period + 1):
    patients_count = int(input())

    if days % 3 == 0:
        if untreated_patients > treated_patients:
            doctor_count += 1

    if patients_count <= doctor_count:
        treated_patients += patients_count

    elif patients_count > doctor_count:
        untreated_patients += patients_count - doctor_count
        treated_patients += doctor_count

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')