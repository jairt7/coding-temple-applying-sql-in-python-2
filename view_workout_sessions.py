from connect_mysql import connect_database

def view_workout_sessions():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = "SELECT * FROM WorkoutSessions"
            
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