from connect_mysql import connect_database

def check_if_exists(member_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            id = (member_id, )
            query = "SELECT COUNT(*) FROM Members WHERE id = %s"

            cursor.execute(query, id)
            count = cursor.fetchone()[0]
            if count:
                return True
            else:
                return False
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()


def update_age(member_id, age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_age = (age, member_id)

            query = "UPDATE Members SET age = %s WHERE id = %s;"

            cursor.execute(query, new_age)
            conn.commit()
            print("New member added successfully.")

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()