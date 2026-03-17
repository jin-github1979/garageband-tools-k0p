import os
import shutil

def ensure_directory_exists(directory: str):
    """Ensure that the given directory exists; if not, create it."""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")
    except Exception as e:
        print(f"Error creating directory {directory}: {e}")

def copy_file(src: str, dst: str):
    """Copy a file from src to dst. Raise error if the source file doesn't exist."""
    try:
        if not os.path.isfile(src):
            raise FileNotFoundError(f"Source file does not exist: {src}")
        shutil.copy2(src, dst)
        print(f"Copied file from {src} to {dst}")
    except Exception as e:
        print(f"Error copying file from {src} to {dst}: {e}")

def read_file_lines(file_path: str):
    """Read lines from a file and return as a list. Handle file not found errors."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        print(f"Read {len(lines)} lines from {file_path}")
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def write_lines_to_file(file_path: str, lines: list):
    """Write a list of lines to a file. Overwrites the file if it already exists."""
    try:
        with open(file_path, 'w') as f:
            f.writelines(lines)
        print(f"Wrote {len(lines)} lines to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def delete_file(file_path: str):
    """Delete a file if it exists. Print a message regardless of success."""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        else:
            print(f"File not found, cannot delete: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

# TODO: Consider adding more utility functions as needed, like moving files or zipping directories.
# Note: This file could grow to include more sophisticated file operations as the project evolves.
