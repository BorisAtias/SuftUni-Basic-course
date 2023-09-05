text = input().lower()
vowels_value = 0

for letter in text:
    if letter == 'a':
        vowels_value += 1
    elif letter == 'e':
        vowels_value += 2
    elif letter == 'i':
        vowels_value += 3
    elif letter == 'o':
        vowels_value += 4
    elif letter == 'u':
        vowels_value += 5
print(vowels_value)