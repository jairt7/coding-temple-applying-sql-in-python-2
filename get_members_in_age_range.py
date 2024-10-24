from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = "SELECT * FROM Members WHERE Age BETWEEN 25 AND 30"
            
            cursor.execute(query)
            
            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")
            
        finally:
            cursor.close()
            conn.close()

    else:
        print("Couldn't find the database.")