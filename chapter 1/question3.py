import os

def print_directory_contents(directory):
    try:
        # List all the contents of the directory
        contents = os.listdir(directory)
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

# Get the current working directory
current_directory = os.getcwd()

# Print the contents of the current directory
print_directory_contents(current_directory)
