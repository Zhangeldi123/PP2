from functools import reduce


user_input = input("Enter a list of numbers separated by spaces: ")


numbers_list = list(map(float, user_input.split()))


if numbers_list:
    
    result = reduce(lambda x, y: x * y, numbers_list)
    print(f"The product of the numbers in the list {numbers_list} is: {result}")
else:
    print("The input list is empty.")