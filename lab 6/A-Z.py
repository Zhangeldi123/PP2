for char in range(ord('A'), ord('Z')+1):
    file_name = f"{chr(char)}.txt"
    
    
    with open(file_name, 'w') as file:
        file.write(f"This is file {chr(char)}.")

print("Text files created successfully.")