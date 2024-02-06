def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, user_input.split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers_list))

print("Original list:", numbers_list)
print("Prime numbers:", prime_numbers)