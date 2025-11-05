# Lesson 6: In-Class Assignments

Complete these assignments during the live lesson. Each assignment builds on the concepts covered in the lesson.

---

## Assignment 1: Simple Many-to-Many Relationship

**Goal:** Create a many-to-many relationship between Students and Clubs

### Tasks:
1. **Create an association table** for students and clubs
   - Use `Table()` with `student_id` and `club_id` as ForeignKeys

2. **Create Student model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `email` (String)
   - `clubs` (relationship to clubs)

3. **Create Club model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `description` (String)
   - `students` (relationship to students)



---

## Assignment 2: Association Model with Additional Data

**Goal:** Create a many-to-many relationship between Books and Readers with extra information

### Tasks:
1. **Create BookReader association model** with:
   - `book_id` (ForeignKey to books)
   - `reader_id` (ForeignKey to readers)
   - `rating` (Float)
   - `review_date` (DateTime)

2. **Create Book model** with:
   - `id` (Integer, primary key)
   - `title` (String)
   - `author` (String)
   - `readers` (relationship to BookReader)

3. **Create Reader model** with:
   - `id` (Integer, primary key)
   - `name` (String)
   - `email` (String)
   - `books` (relationship to BookReader)



---