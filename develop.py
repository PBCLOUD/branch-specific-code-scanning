import sqlite3
import os

def get_user_data(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

# Insecure eval example
def execute_code(user_input):
    # Warning: This is a dangerous use of eval()
    result = eval(user_input)
    return result

# Hardcoded credentials example
def connect_to_db():
    username = "admin"
    password = "password123"
    conn = sqlite3.connect(f'secret.db?user={username}&password={password}')
    return conn

def main():
    # Test SQL Injection
    user_id = "1 OR 1=1"  # This input is intended to cause SQL injection
    print("Fetching user data with SQL Injection:")
    print(get_user_data(user_id))

    # Test insecure eval
    user_code = "2 + 2"  # Simple example; replace with more complex input
    print("Evaluating user code:")
    print(execute_code(user_code))

    # Test hardcoded credentials
    print("Connecting to database with hardcoded credentials:")
    conn = connect_to_db()
    if conn:
        print("Connection successful!")
    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()
