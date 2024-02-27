import re

def replace_characters(input_string):
    pattern = re.compile(r'[ ,.]')
    replaced_string = re.sub(pattern, ':', input_string)
    return replaced_string

user_input = input("Enter a string: ")
result = replace_characters(user_input)
print(f"Result: {result}")