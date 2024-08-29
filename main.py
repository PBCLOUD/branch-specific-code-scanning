import sqlite3

def get_user_data(username):
    # Establish a database connection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Insecure: Directly incorporating user input into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    # Fetch and print the user data
    user_data = cursor.fetchall()
    print(user_data)
    
    # Close the connection
    conn.close()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a username: ")
    get_user_data(user_input)
