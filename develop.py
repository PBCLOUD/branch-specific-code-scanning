# develop.py
import os

def delete_file(file_path):
    os.system(f"rm {file_path}")  # Potential command injection vulnerability

delete_file("important_file.txt")
