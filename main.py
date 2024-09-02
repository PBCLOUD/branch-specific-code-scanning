import sqlite3
import os
import subprocess

def get_user_data(username):
    # Establish a database connection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Insecure: Directly incorporating user input into SQL query (SQL Injection Vulnerability)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    # Fetch and print the user data
    user_data = cursor.fetchall()
    print(user_data)
    
    # Close the connection
    conn.close()

def execute_command(command):
    # Insecure: Directly executing user input (Command Injection Vulnerability)
    subprocess.run(command, shell=True)

def read_file(file_path):
    # Insecure: Using user input to open files (Path Traversal Vulnerability)
    with open(file_path, 'r') as file:
        content = file.read()
    print(content)

def insecure_function():
    # Insecure: Hardcoded sensitive data (Sensitive Data Exposure)
    password = 'password123'
    print(f"Password is: {password}")

# Example usage
if __name__ == "__main__":
    # Simulate user input that could be malicious
    user_input = "admin' OR '1'='1"
    get_user_data(user_input)
    
    # Simulate command injection
    command_input = "ls -la; echo Hello"
    execute_command(command_input)
    
    # Simulate path traversal
    file_input = "../../etc/passwd"
    read_file(file_input)
    
    # Example of insecure function
    insecure_function()
