def get_remaining_alphabet(start_letter):
    if start_letter.isalpha() and len(start_letter) == 1:
        start_ord = ord(start_letter)
        if start_letter.islower():
            end_ord = ord('z')
        elif start_letter.isupper():
            end_ord = ord('Z')
        else:
            return "Invalid input: letter must be a-z or A-Z."

        letters = [chr(i) for i in range(start_ord, end_ord + 1)]
        return "".join(letters)
    else:
        return "Invalid input: please enter a single letter (a-z or A-Z)."


user_letter = input("Enter a letter (a-z or A-Z): ")
result_string = get_remaining_alphabet(user_letter)
print(result_string)
