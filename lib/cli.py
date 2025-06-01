from datetime import datetime
from lib.models import Session, Swimmer, Instructor, Enrollment

def list_swimmers():
    session = Session()
    swimmers = session.query(Swimmer).all()
    print("\nList of Swimmers:")
    for s in swimmers:
        print(f"{s.id}: {s.name}, Age: {s.age}, Level: {s.level}")
    session.close()

def add_swimmer():
    name = input("Enter swimmer name: ").strip()
    age = input("Enter swimmer age: ").strip()
    level = input("Enter swimmer level (Beginner, Intermediate, Advanced): ").strip().capitalize()

    if level not in ['Beginner', 'Intermediate', 'Advanced']:
        print("❌ Invalid level! Must be Beginner, Intermediate, or Advanced.")
        return

    try:
        age = int(age)
    except ValueError:
        print("❌ Age must be a number.")
        return

    swimmer = Swimmer(name=name, age=age, level=level)
    session = Session()
    session.add(swimmer)
    session.commit()
    print(f"✅ Added swimmer: {swimmer.name}, Age: {swimmer.age}, Level: {swimmer.level}")
    session.close()

def list_instructors():
    session = Session()
    instructors = session.query(Instructor).all()
    print("\nList of Instructors:")
    for i in instructors:
        print(f"{i.id}: {i.name}, Email: {i.email}, Certified Level: {i.certified_level}, Experience: {i.years_experience} years")
    session.close()

def add_instructor():
    name = input("Enter instructor name: ").strip()
    email = input("Enter instructor email: ").strip()
    certified_level = input("Enter certified level (Beginner, All Levels): ").strip().title()
    years_exp = input("Enter years of experience: ").strip()

    if certified_level not in ['Beginner', 'All Levels']:
        print("❌ Invalid certified level! Must be 'Beginner' or 'All Levels'.")
        return

    try:
        years_exp = int(years_exp)
    except ValueError:
        print("❌ Years of experience must be a number.")
        return

    instructor = Instructor(name=name, email=email, certified_level=certified_level, years_experience=years_exp)
    session = Session()
    session.add(instructor)
    session.commit()
    print(f"✅ Added instructor: {instructor.name}, Email: {instructor.email}, Certified Level: {instructor.certified_level}")
    session.close()

def list_enrollments():
    session = Session()
    enrollments = session.query(Enrollment).all()
    print("\nList of Enrollments:")
    if not enrollments:
        print("No enrollments yet.")
    for e in enrollments:
        swimmer = e.swimmer
        instructor = e.instructor
        print(f"{e.id}: Swimmer: {swimmer.name} (Level: {swimmer.level}) -> Instructor: {instructor.name} (Cert: {instructor.certified_level}), Date: {e.session_date}")
    session.close()

def enroll_swimmer():
    session = Session()

    swimmers = session.query(Swimmer).all()
    if not swimmers:
        print("❌ No swimmers available.")
        session.close()
        return
    print("\nSwimmers:")
    for s in swimmers:
        print(f"{s.id}: {s.name}, Level: {s.level}")

    try:
        swimmer_id = int(input("Enter swimmer ID to enroll: ").strip())
        swimmer = session.query(Swimmer).filter_by(id=swimmer_id).first()
        if not swimmer:
            raise ValueError("Swimmer not found.")
    except ValueError as e:
        print(f"❌ {e}")
        session.close()
        return

    instructors = session.query(Instructor).all()
    if not instructors:
        print("❌ No instructors available.")
        session.close()
        return
    print("\nInstructors:")
    for i in instructors:
        print(f"{i.id}: {i.name}, Certified Level: {i.certified_level}")

    try:
        instructor_id = int(input("Enter instructor ID: ").strip())
        instructor = session.query(Instructor).filter_by(id=instructor_id).first()
        if not instructor:
            raise ValueError("Instructor not found.")
    except ValueError as e:
        print(f"❌ {e}")
        session.close()
        return

    session_date_input = input("Enter session date (YYYY-MM-DD) or press Enter for today: ").strip()
    try:
        session_date = datetime.strptime(session_date_input, "%Y-%m-%d").date() if session_date_input else datetime.today().date()
    except ValueError:
        print("❌ Invalid date format.")
        session.close()
        return

    enrollment = Enrollment(swimmer_id=swimmer_id, instructor_id=instructor_id, session_date=session_date)
    session.add(enrollment)
    session.commit()
    print(f"✅ Enrolled: {swimmer.name} with Instructor {instructor.name} on {session_date}")
    session.close()

def reset_all_data():
    confirm = input("Are you sure you want to delete ALL data? This cannot be undone. (yes/no): ").strip().lower()
    if confirm != "yes":
        print("❌ Reset cancelled.\n")
        return

    session = Session()
    session.query(Enrollment).delete()
    session.query(Swimmer).delete()
    session.query(Instructor).delete()
    session.commit()
    session.close()
    print("✅ All data has been reset.\n")

def main_menu():
    while True:
        print("\nSwim Class Enrollment CLI")
        print("1. List Swimmers")
        print("2. Add Swimmer")
        print("3. List Instructors")
        print("4. Add Instructor")
        print("5. List Enrollments")
        print("6. Enroll Swimmer")
        print("7. Reset All Data")
        print("8. Quit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            list_swimmers()
        elif choice == '2':
            add_swimmer()
        elif choice == '3':
            list_instructors()
        elif choice == '4':
            add_instructor()
        elif choice == '5':
            list_enrollments()
        elif choice == '6':
            enroll_swimmer()
        elif choice == '7':
            reset_all_data()
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
