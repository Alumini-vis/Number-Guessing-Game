import os

def get_directory_size(path):

    """Recursively calculates the total size of a directory and its files."""
    total_size = 0

    # Base Case: If the path is a file, return its size.
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except OSError as e:
            print(f"Error reading file {path}: {e}")
            return 0

    # Recursive Case: If the path is a directory, iterate through its contents.
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            total_size += get_directory_size(full_path)
    except OSError as e:
        print(f"Error accessing directory {path}: {e}")

    return total_size

if __name__ == "__main__":
    directory = input("Enter the directory path to calculate its size: ").strip()

    # Input validation: Check if the provided path exists and is a directory.
    if not os.path.isdir(directory):
        print(f"The path '{directory}' doesn't exist.")
    else:
        size_byte = get_directory_size(directory)
        size_mb = size_byte / (1024 * 1024) # Convert bytes to megabytes
        print(f"The total size: {size_byte} bytes ({size_mb:.2f} MB)")