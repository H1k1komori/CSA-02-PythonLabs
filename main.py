lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = lowercase_alphabet + uppercase_alphabet

user_input = input("Enter a range of letters (a-z, A-Z): ")

finish_letter: object
begin_letter, finish_letter = user_input.split("-")

index_of_start = alphabet.find(begin_letter)
index_of_finish = alphabet.find(finish_letter) + 1

subset_of_alphabet = alphabet[index_of_start:index_of_finish]

print(subset_of_alphabet)