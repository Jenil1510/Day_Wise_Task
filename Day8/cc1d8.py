class FileReadError(Exception):
    """Custom exception class for file reading errors."""
    pass

class FileNotFoundError(FileReadError):
    """Exception class for handling file not found errors."""
    pass

class FileReadPermissionError(FileReadError):
    """Exception class for handling file read permission errors."""
    pass

def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise FileReadPermissionError(f"Permission denied while reading file: {file_path}")
    except Exception as e:
        raise FileReadError(f"An error occurred while reading the file: {e}")

# Example usage
file_path = 'example.txt'

try:
    read_and_print_file(file_path)
except FileReadError as e:
    print(f"Error: {e}")
