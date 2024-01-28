def get_alphabet_sequence(input_string):
    if '-' in input_string:
        parts = input_string.split('-')
        if len(parts) == 2 and all(part.isalpha() and len(part) == 1 for part in parts):
            start_letter, end_letter = parts
            start_ord = ord(start_letter)
            end_ord = ord(end_letter)
            if (start_letter.islower() and end_letter.islower()) or (start_letter.isupper() and end_letter.isupper()):
                if start_ord <= end_ord:
                    letters = [chr(i) for i in range(start_ord, end_ord + 1)]
                    return "".join(letters)
                else:
                    return "Invalid range: start letter comes after end letter."
            else:
                return "Invalid input: range letters must both be either lowercase or uppercase."
        else:
            return "Invalid input: range must be in the format 'a-b' or 'A-B'."
    elif input_string.isalpha() and len(input_string) == 1:
        start_ord = ord(input_string)
        if input_string.islower():
            end_ord = ord('z')
        elif input_string.isupper():
            end_ord = ord('Z')
        else:
            return "Invalid input: letter must be a-z or A-Z."
        letters = [chr(i) for i in range(start_ord, end_ord + 1)]
        return "".join(letters)
    else:
        return "Invalid input: please enter a single letter (a-z or A-Z) or a letter range (a-b or A-B)."


user_input = input("Enter a letter or a range of letters (a-z, A-Z): ")
result_string = get_alphabet_sequence(user_input)
print(result_string)
