from sqlalchemy import create_engine, Integer, String, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///school2.db')

Base = declarative_base() #Will be inherited by all model classes, so they can behave as tables

student_clubs = Table( #Association Table Object
    "student_clubs", 
    Base.metadata, 
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("club_id", Integer, ForeignKey("clubs.id")))

class Students(Base):
  __tablename__ = "students"

  id: Mapped[int] = mapped_column(primary_key=True)
  first_name: Mapped[str] = mapped_column(String(80), nullable=False)
  last_name: Mapped[str] = mapped_column(String(80), nullable=False)
  parent_email: Mapped[str] = mapped_column(String(360), nullable=False)

  student_enrollments: Mapped[list['Enrollments']] = relationship("Enrollments", back_populates='enrollment_student')
  clubs_students: Mapped[list['Clubs']] = relationship("Clubs", secondary=student_clubs, back_populates="students")

class Enrollments(Base): #Association Model
  __tablename__ = "enrollments"

  id: Mapped[int] = mapped_column(primary_key=True)
  student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
  course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id'))
  enrollment: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
  notes: Mapped[str] = mapped_column(String(500))
  grade: Mapped[str] = mapped_column(String(2))

  enrollment_student: Mapped['Students'] = relationship('Students', back_populates='student_enrollments')
  enrollments_courses: Mapped['Courses'] = relationship('Courses', back_populates='course_enrollments')

class Courses(Base):
  __tablename__ = "courses"

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(250), nullable=False)
  instructor: Mapped[str] = mapped_column(String(250))

  course_enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='enrollments_courses')

class Clubs(Base):
  __tablename__ = "clubs"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(150), nullable=False)
  description: Mapped[str] = mapped_column(String(950), nullable=False)
  
  students: Mapped[list["Students"]] = relationship("Students", secondary=student_clubs, back_populates="clubs_students")

Session = sessionmaker(bind=engine) # Creating a session class
session = Session() #Creating an instance of session

# Create a student Using our Students model
# alice = Students(first_name="Alice", last_name='Wonderland', parent_email='email@email.com')
# session.add(alice) #adding the new student object to my database session
# session.commit() #Finalizing adding the new student to the database by committing the session

# Create a new course using our Course Model
# history = Courses(title="History", instructor="Dr. Branett")
# session.add(history)
# session.commit()

# Enrolling Alice into History
# new_enrollment = Enrollments(student_id=1, course_id=1, notes="Just beginning the course", grade="A")
# session.add(new_enrollment)
# session.commit()

student = session.get(Students, 1) #SELECT * FROM students WHERE id = 1;
print(student)
print(student.first_name)
print(student.last_name)
print(student.parent_email)
print(student.student_enrollments[0].grade)
print(student.student_enrollments[0].enrollments_courses.title)
print(student.student_enrollments[0].enrollments_courses.instructor)

Base.metadata.create_all(bind=engine)