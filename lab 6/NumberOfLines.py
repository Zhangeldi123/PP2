def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


file_path = input("Enter the path of the text file: ")


lines_count = count_lines(file_path)


if lines_count is not None:
    print(f"The number of lines in the file '{file_path}' is: {lines_count}")