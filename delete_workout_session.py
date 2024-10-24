from connect_mysql import connect_database

def check_if_session_exists(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            id = (session_id, )
            query = "SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s"

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


def delete_session(session_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            deleted_session = (session_id, )

            query = "DELETE FROM WorkoutSessions WHERE session_id = %s;"

            cursor.execute(query, deleted_session)
            conn.commit()
            print("Workout session deleted.")

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()