from connect_mysql import connect_database

def add_workout_session(member_id, session_date, session_time, activity):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            new_workout_session = (member_id, session_date, session_time, activity)

            query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_workout_session)
            conn.commit()
            print("New member added successfully.")

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()