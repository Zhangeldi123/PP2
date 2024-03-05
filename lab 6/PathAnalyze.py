import os

def analyze_path(input_path):
    
    if os.path.exists(input_path):
        
        filename = os.path.basename(input_path)
        directory = os.path.dirname(input_path)

        print(f"Path '{input_path}' exists.")
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")

    else:
        print(f"Path '{input_path}' does not exist.")


user_input = input("Enter a path to analyze: ")


analyze_path(user_input)