CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY,
    faculty_name VARCHAR(50)
);

CREATE TABLE Department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50),
    faculty_id INT REFERENCES Faculty (faculty_id) ON DELETE CASCADE
);

CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(50),
    department_id INT REFERENCES Department (department_id) ON DELETE CASCADE
);

CREATE TABLE CourseOutline (
    outline_id SERIAL PRIMARY KEY,
    outline_description TEXT,
    course_id INT REFERENCES Course (course_id) ON DELETE CASCADE
);

CREATE TABLE Semester (
    semester_id SERIAL PRIMARY KEY,
    semester_name VARCHAR(50),
    start_date DATE,
    end_date DATE
);

CREATE TABLE Class (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(50),
    course_id INT REFERENCES Course (course_id) ON DELETE CASCADE,
    semester_id INT REFERENCES Semester (semester_id) ON DELETE CASCADE
);

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE
);

CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT REFERENCES Department (department_id) ON DELETE CASCADE
);

CREATE TABLE Building (
    building_id SERIAL PRIMARY KEY,
    building_name VARCHAR(50)
);

CREATE TABLE Classroom (
    classroom_id SERIAL PRIMARY KEY,
    classroom_name VARCHAR(50),
    building_id INT REFERENCES Building (building_id) ON DELETE CASCADE
);

CREATE TABLE Schedule (
    schedule_id SERIAL PRIMARY KEY,
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE,
    teacher_id INT REFERENCES Teacher (teacher_id) ON DELETE CASCADE,
    classroom_id INT REFERENCES Classroom (classroom_id) ON DELETE CASCADE,
    start_time TIME,
    end_time TIME
);

CREATE TABLE Grade (
    grade_id SERIAL PRIMARY KEY,
    grade_value INT,
    student_id INT REFERENCES Student (student_id) ON DELETE CASCADE,
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE
);

CREATE TABLE Exam (
    exam_id SERIAL PRIMARY KEY,
    exam_name VARCHAR(50),
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE
);

CREATE TABLE Homework (
    homework_id SERIAL PRIMARY KEY,
    homework_name VARCHAR(50),
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE,
    creation_date DATE
);

CREATE TABLE Syllabus (
    syllabus_id SERIAL PRIMARY KEY,
    syllabus_name VARCHAR(50),
    class_id INT REFERENCES Class (class_id) ON DELETE CASCADE
);
