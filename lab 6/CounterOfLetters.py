def count_upper_lower(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    return upper_count, lower_count


user_input = input("Enter a string: ")

upper, lower = count_upper_lower(user_input)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")