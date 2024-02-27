import re

def snake_to_camel(snake_case_string):
    words = re.split('_+', snake_case_string)
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string


snake_case_input = input("Enter a snake_case string: ")
camel_case_output = snake_to_camel(snake_case_input)
print(f"CamelCase output: {camel_case_output}")