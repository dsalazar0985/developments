import os
import logging

def create_file_in_home(filename, content, max_attempts=3):
    home_directory = os.path.expanduser("~")
    file_path = os.path.join(home_directory, filename)
    
    # Configurar el logging
    log_file = "/var/log/ntwrsla.log"
    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            
            file_size = os.path.getsize(file_path)
            if file_size >= 10 * 1024:  # 10 KB in bytes
                print(f"File '{filename}' created successfully in {home_directory}")
                return
            else:
                print(f"Attempt {attempts + 1}: File size is less than 10 KB, retrying...")
                attempts += 1
        
        except PermissionError as e:
            error_message = "Permission denied: You don't have write access to the /home directory."
            print(error_message)
            logging.error(error_message)
            return
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            logging.error(error_message)
            return
    
    error_message = "Error: Could not create the file with a size of at least 10 KB after 3 attempts."
    print(error_message)
    logging.error(error_message)

if __name__ == "__main__":
    filename = "example.txt"
    content = "This is a sample file."
    create_file_in_home(filename, content)
