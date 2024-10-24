from connect_mysql import connect_database

def add_members(name, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_member = (name, age)

            query = "INSERT INTO Members (name, age) VALUES (%s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New member added successfully.")

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()