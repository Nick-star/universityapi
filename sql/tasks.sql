-- 1
SELECT Student.* FROM Student
JOIN Class ON Student.class_id = Class.class_id
JOIN Course ON Class.course_id = Course.course_id
WHERE Course.course_name = 'Математика';


-- 2
CREATE OR REPLACE FUNCTION update_student_grade(p_student_id INT, p_class_id INT, p_grade_value INT)
RETURNS VOID AS
$$
BEGIN
    UPDATE Grade SET grade_value = p_grade_value
    WHERE student_id = p_student_id AND class_id = p_class_id;
END
$$
LANGUAGE 'plpgsql';

SELECT update_student_grade(1, 1, 5);

-- 3
SELECT Teacher.* FROM Teacher
JOIN Schedule ON Teacher.teacher_id = Schedule.teacher_id
JOIN Classroom ON Schedule.classroom_id = Classroom.classroom_id
WHERE Classroom.building_id = 3;

-- 4
DELETE FROM Homework
WHERE creation_date < NOW() - INTERVAL '1 year';

-- 5
CREATE OR REPLACE FUNCTION insert_new_semester(p_semester_name VARCHAR, p_start_date DATE, p_end_date DATE)
RETURNS VOID AS
$$
BEGIN
    INSERT INTO Semester (semester_name, start_date, end_date)
    VALUES (p_semester_name, p_start_date, p_end_date);
END
$$
LANGUAGE 'plpgsql';

SELECT insert_new_semester('Весна 2024', '2024-01-01', '2024-05-31');
