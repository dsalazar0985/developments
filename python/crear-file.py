import os

def create_file_in_home(filename, content):
    home_directory = os.path.expanduser("~")
    file_path = os.path.join(home_directory, filename)
    
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{filename}' created successfully in {home_directory}")
    except PermissionError:
        print("Permission denied: You don't have write access to the /home directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = "file_test.txt"
    content = "This is a sample file."
    create_file_in_home(filename, content)
