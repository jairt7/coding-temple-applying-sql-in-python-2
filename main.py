from connect_mysql import connect_database
from add_member import add_members
from view_members import view_members
from view_workout_sessions import view_workout_sessions
from add_workout_session import add_workout_session
from update_age import update_age, check_if_exists
from delete_workout_session import check_if_session_exists, delete_session
from get_members_in_age_range import get_members_in_age_range

def welcome_message():
    print("Welcome to my SQL homework.")
    print("1. Display all members")
    print("2. Display all workout sessions")
    print("3. Add a new member")
    print("4. Add a workout session for a member")
    print("5. Update a member's age")
    print("6. Delete a workout session")
    print("7. Quit")

keep_going = True

def main_menu():
    global keep_going
    what_to_do = input("What would you like to do? ")
    if what_to_do == "1":
        view_members()

    elif what_to_do == "2":
        view_workout_sessions()

    elif what_to_do == "3":
        name = input("What is the name of the new member? ")
        age = int(input("How old is the new member? Enter a number: "))
        add_members(name, age)

    elif what_to_do == "4":
        try:
            member_id = int(input("What is the member's ID number? "))
        except ValueError:
            print("That's not a number. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")
        session_date = input("What is the date of the workout session? Format: YYYY-MM-DD: ")
        session_time = input("What time is the session? ")
        activity = input("What is the activity the member will be doing? ")
        add_workout_session(member_id, session_date, session_time, activity)

    elif what_to_do == "5":
        try:
            member_id = int(input("What is the member ID of the member you'd like to update? "))
            exists = check_if_exists(member_id)
            if exists:
                try:
                    new_age = int(input("Please enter the member's new age: "))
                    update_age(member_id, new_age)
                except ValueError:
                    print("That's not a number. Please enter a number.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("That member wasn't found in the database.")
        except ValueError:
            print("That's not a number. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

    elif what_to_do == "6":
        try:
            delete_this_session = int(input("What is the session ID of the workout session you'd like to delete? "))
            exists = check_if_session_exists(delete_this_session)
            if exists:
                try:
                    delete_session(delete_this_session)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("That workout session wasn't found in the database.")
        except ValueError:
            print("That's not a number. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")
    
    elif what_to_do == "7":
        print("Thanks for using my program. Let me know if I need to improve anything.")
        print("Also, here's that part 2 of the assignment:")
        start_age = 25
        end_age = 30
        get_members_in_age_range(start_age, end_age)
        keep_going = False
    else:
        print("That's not a number. Please enter a number from 1 to 7.")

while keep_going:
    welcome_message()
    main_menu()