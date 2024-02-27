import re

def match_string(input_string):
    pattern = re.compile(r'a(bb|bbb)')
    match = pattern.search(input_string)

    if match:
        print(f"Match found: {match.group()}")
    else:
        print("No match found")

while True:
    user_input = input("Enter a string (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    match_string(user_input)
    print()