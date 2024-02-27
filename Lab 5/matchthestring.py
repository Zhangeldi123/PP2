import re

def match_pattern(input_string):
    pattern = re.compile(r'a*b*')

    matches_findall = pattern.findall(input_string)
    if matches_findall:
        print(f"Using findall: Found matches in '{input_string}': {matches_findall}")
    else:
        print(f"Using findall: No matches found in '{input_string}'")
input_string = input("Enter a string: ")
match_pattern(input_string)