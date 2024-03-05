import os

def check_path_access(path):
    try:
        
        if not os.path.exists(path):
            print(f"Error: Path '{path}' does not exist.")
            return

        
        if os.access(path, os.R_OK):
            print(f"Read access to '{path}' is granted.")
        else:
            print(f"Read access to '{path}' is denied.")

        
        if os.access(path, os.W_OK):
            print(f"Write access to '{path}' is granted.")
        else:
            print(f"Write access to '{path}' is denied.")

        
        if os.access(path, os.X_OK):
            print(f"Execute access to '{path}' is granted.")
        else:
            print(f"Execute access to '{path}' is denied.")

    except Exception as e:
        print(f"An error occurred: {e}")


specified_path = input("Enter the path to check for access: ")


check_path_access(specified_path)
