def unique_elements_from_input():
    input_list = input("Enter a list of numbers separated by spaces: ").split()
    input_list = [int(item) for item in input_list]  # Convert input to integers

    unique_list = []

    for element in input_list:
        if input_list.count(element) == 1:
            unique_list.append(element)

    return unique_list

result = unique_elements_from_input()

print("List with unique elements:", result)