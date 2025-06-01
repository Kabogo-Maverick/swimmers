from lib.models import Base, engine
from lib.cli import main_menu

if __name__ == '__main__':
    print("Creating swimmers and instructors tables...")
    Base.metadata.create_all(engine)
    # print("All tables created successfully.")
    main_menu()
