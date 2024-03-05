def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"Data written to file '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


user_input = input("Enter a list of strings separated by spaces: ")
my_list = user_input.split()


file_path = input("Enter the file path to write the list: ")


write_list_to_file(file_path, my_list)