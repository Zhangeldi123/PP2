import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all_contents = os.listdir(path)
    return all_contents


specified_path = input("Enter the path to list directories and files: ")


directories_list = list_directories(specified_path)
print("Directories:", directories_list)


files_list = list_files(specified_path)
print("Files:", files_list)


all_list = list_all(specified_path)
print("All Contents:", all_list)