def squares(a, b):
    for i in range(a, b+1):
        yield i**2

user_inputa = int(input("Enter bottom number "))
user_inputb = int(input("Enter the top value: "))
for square in squares(user_inputa, user_inputb):
    print(square)