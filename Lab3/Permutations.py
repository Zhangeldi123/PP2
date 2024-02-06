from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")


    for perm in permutations(user_input):
        print(''.join(perm))


print_permutations()