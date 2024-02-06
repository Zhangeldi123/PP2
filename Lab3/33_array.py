def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Enter a list of integers separated by spaces: ")
nums_list = list(map(int, user_input.split()))
result = has_33(nums_list)

print(f"List contains 3 next to 3: {result}")

def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

user_input = input("Enter a list of integers separated by spaces: ")
nums_list = list(map(int, user_input.split()))
result = contains_007(nums_list)

print(f"List contains 007 in order: {result}")