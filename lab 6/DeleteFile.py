import os

def delete_file(file_path):
    try:
        
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            return

        
        if not os.access(file_path, os.W_OK):
            print(f"Error: Permission denied. Unable to delete file '{file_path}'.")
            return

        
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = input("Enter the path of the file to delete: ")


delete_file(file_path)