import re

def split_at_uppercase(input_string):
    result = re.split(r'(?=[A-Z])[a-z]*', input_string)
    return result[1:]


input_string = input("Enter a string: ")
split_result = split_at_uppercase(input_string)
print(f"Split result: {split_result}")