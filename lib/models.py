from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Connect to SQLite DB
engine = create_engine("sqlite:///db/swim_class.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Swimmer(Base):
    __tablename__ = 'swimmers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    level = Column(String, nullable=False)

    __table_args__ = (
        CheckConstraint(level.in_(['Beginner', 'Intermediate', 'Advanced']), name="valid_swimmer_level"),
    )

    enrollments = relationship("Enrollment", back_populates="swimmer")

    def __repr__(self):
        return f"<Swimmer(name='{self.name}', age={self.age}, level='{self.level}')>"

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    certified_level = Column(String, nullable=False)
    years_experience = Column(Integer, default=0)

    __table_args__ = (
        CheckConstraint(certified_level.in_(['Beginner', 'Intermediate', 'Advanced', 'All Levels']), name="valid_certified_level"),
    )

    enrollments = relationship("Enrollment", back_populates="instructor")

    def __repr__(self):
        return f"<Instructor(name='{self.name}', certified_level='{self.certified_level}')>"

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    swimmer_id = Column(Integer, ForeignKey('swimmers.id'))
    instructor_id = Column(Integer, ForeignKey('instructors.id'))

    swimmer = relationship("Swimmer", back_populates="enrollments")
    instructor = relationship("Instructor", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment(swimmer_id={self.swimmer_id}, instructor_id={self.instructor_id})>"

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("All tables created successfully.")
