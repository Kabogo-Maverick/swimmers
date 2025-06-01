from lib.models import Session, Swimmer, Instructor, Enrollment, Base, engine

def reset_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def seed_data():
    session = Session()

    instructor1 = Instructor(name="Coach Alice", email="alice@swim.com", certified_level="Beginner", years_experience=3)
    instructor2 = Instructor(name="Coach Ben", email="ben@swim.com", certified_level="All Levels", years_experience=7)

    swimmer1 = Swimmer(name="Liam", age=8, level="Beginner")
    swimmer2 = Swimmer(name="Sophia", age=10, level="Intermediate")
    swimmer3 = Swimmer(name="Ethan", age=12, level="Advanced")

    enrollment1 = Enrollment(swimmer=swimmer1, instructor=instructor1)
    enrollment2 = Enrollment(swimmer=swimmer2, instructor=instructor2)
    enrollment3 = Enrollment(swimmer=swimmer3, instructor=instructor2)

    session.add_all([instructor1, instructor2, swimmer1, swimmer2, swimmer3, enrollment1, enrollment2, enrollment3])
    session.commit()
    session.close()

    print("✅ Seed data added successfully.")

if __name__ == '__main__':
    reset_tables()
    seed_data()
