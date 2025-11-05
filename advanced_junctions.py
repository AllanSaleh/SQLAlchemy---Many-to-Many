from sqlalchemy import create_engine, Integer, String, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
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

Base.metadata.create_all(bind=engine)