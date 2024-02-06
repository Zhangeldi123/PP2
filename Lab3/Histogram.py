def histogram():
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]

    print(' '.join('*' * num for num in numbers))

histogram()
