import sqlite3

def get_table_names(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # Use a query to get the table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    
    # Fetch all the table names
    table_names = cursor.fetchall()

    # Close the connection
    connection.close()

    return table_names

# Example usage
database_file_path = "FridayProj5.db"
tables = get_table_names(database_file_path)

for table in tables:
    print(table[0])
