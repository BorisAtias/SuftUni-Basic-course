import string

main_string = string.ascii_letters
first_word = ''
final_string = ''

c_counter = 0
o_counter = 0
n_counter = 0

end = 'End'

while end == "End":

    if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
        first_word += ' '
        final_string += first_word
        first_word = ''
        c_counter = 0
        o_counter = 0
        n_counter = 0

    letter = input()

    if letter == "End":
        break

    if letter == 'c':
        c_counter += 1

        if c_counter > 1:
            first_word += letter
        continue

    if letter == 'o':
        o_counter += 1

        if o_counter > 1:
            first_word += letter
        continue

    if letter == 'n':
        n_counter += 1

        if n_counter > 1:
            first_word += letter
        continue

    if letter in main_string:
        first_word += letter

print(final_string)