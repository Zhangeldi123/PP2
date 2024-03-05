def is_palindrome(s):

    s = s.lower()
    
    
    s = ''.join(char for char in s if char.isalnum())

    return s == s[::-1]

user_input = input("Enter a string to check for palindrome: ")

if is_palindrome(user_input):
    print(f"The string '{user_input}' is a palindrome.")
else:
    print(f"The string '{user_input}' is not a palindrome.")