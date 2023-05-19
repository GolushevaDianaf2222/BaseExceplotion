import sqlite3

class DatabaseException(BaseException):
    pass

def get_user_data(user_id):
    conn = None
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user_data = cursor.fetchone()
        if not user_data:
            raise DatabaseException(f"User with id {user_id} not found")
        return user_data
    except sqlite3.Error as e:
        raise DatabaseException(f"Error: {e}") from e
    finally:
        if conn:
            conn.close()

try:
    print(get_user_data(10))
except DatabaseException as e:
    print(f'Error: {e}')
    
    

 

