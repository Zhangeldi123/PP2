import re

def find_sequences(input_string):
    pattern = re.compile(r'a.+b$')
    matches = pattern.findall(input_string)

    if matches:
        print(f"Sequences found: {matches}")
    else:
        print("No sequences found")


user_input = input("Enter a string: ")
find_sequences(user_input)