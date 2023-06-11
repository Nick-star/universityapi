-- Вставка данных в таблицы
INSERT INTO Faculty (faculty_name) VALUES ('Факультет наук');
INSERT INTO Department (department_name, faculty_id) VALUES ('Отделение математики', 1);
INSERT INTO Course (course_name, department_id) VALUES ('Математика', 1);
INSERT INTO CourseOutline (outline_description, course_id) VALUES ('Введение в Алгебру', 1);
INSERT INTO Semester (semester_name, start_date, end_date) VALUES ('Семестр конца 2023', '2023-09-01', '2023-12-31');
INSERT INTO Class (class_name, course_id, semester_id) VALUES ('Алгебра 101', 1, 1);
INSERT INTO Student (first_name, last_name, class_id) VALUES ('Иван', 'Петров', 1);
INSERT INTO Teacher (first_name, last_name, department_id) VALUES ('Анна', 'Аксёнова', 1);
INSERT INTO Building (building_name) VALUES ('Здание 3');
INSERT INTO Classroom (classroom_name, building_id) VALUES ('Кабинет Алгебры', 1);
INSERT INTO Schedule (class_id, teacher_id, classroom_id, start_time, end_time) VALUES (1, 1, 1, '09:00:00', '10:00:00');
INSERT INTO Grade (grade_value, student_id, class_id) VALUES (4, 1, 1);
INSERT INTO Exam (exam_name, class_id) VALUES ('Математический Аналзи', 1);
INSERT INTO Homework (homework_name, class_id, creation_date) VALUES ('Самостоятельная работа №1', 1, '2022-06-01');
INSERT INTO Syllabus (syllabus_name, class_id) VALUES ('Учебный план №1', 1);
