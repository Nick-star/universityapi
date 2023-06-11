from typing import List

from fastapi import FastAPI, HTTPException
from db_manager import DBManager
from models import Student, StudentCreate, Course, CourseCreate, Grade, GradeCreate, Teacher

app = FastAPI()

# Конфигурационные параметры
db_config = {
    'user': 'postgres',
    'password': 'pass',
    'database': 'university',
    'host': 'db',
    'port': '5432'
}

db_manager = DBManager(db_config)


# Подключение к базе данных при запуске приложения
@app.on_event("startup")
async def startup():
    await db_manager.connect()


# Отключение от базы данных при остановке приложения
@app.on_event("shutdown")
async def shutdown():
    await db_manager.disconnect()


# Роуты для студентов
@app.post("/students", response_model=Student)
async def create_student(student: StudentCreate):
    '''
    Создать нового студента
    POST /students
    Content-Type: application/json

    Ожидаемые параметры:
    {
      "first_name": str,  // Имя студента
      "last_name": str,  // Фамилия студента
      "class_id": int  // Идентификатор класса
    }

    '''
    async with db_manager as manager:
        student_id = await manager.fetchval(
            "INSERT INTO Student (first_name, last_name, class_id) VALUES ($1, $2, $3) RETURNING student_id",
            student.first_name, student.last_name, student.class_id
        )
        return {**student.dict(), "student_id": student_id}


@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: int):
    """
    Получить информацию о студенте по его id
    GET /students/{student_id}
    Accept: application/json

    Параметры:
    student_id - идентификатор студента (целое число)
    """
    async with db_manager as manager:
        student = await manager.fetchrow(
            "SELECT * FROM Student WHERE student_id = $1", student_id
        )
        if student is None:
            raise HTTPException(status_code=404, detail="Студент не найден")
        return Student(**student)


@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: int, student: StudentCreate):
    """
    Обновить информацию о студенте по его id
    PUT /students/{student_id}
    Content-Type: application/json

    Ожидаемые параметры:
    {
      "first_name": str,  // Имя студента
      "last_name": str,  // Фамилия студента
      "class_id": int  // Идентификатор класса
    }

    Параметры:
    student_id - идентификатор студента (целое число)
    """
    async with db_manager as manager:
        updated_student = await manager.fetchrow(
            "UPDATE Student SET first_name = $1, last_name = $2, class_id = $3 WHERE student_id = $4 RETURNING *",
            student.first_name, student.last_name, student.class_id, student_id
        )
        if updated_student is None:
            raise HTTPException(status_code=404, detail="Студент не найден")
        return Student(**updated_student)


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """
    Удалить студента по его id
    DELETE students/{student_id}

    Параметры:
    student_id - идентификатор студента (целое число)
    """
    async with db_manager as manager:
        deleted = await manager.execute(
            "DELETE FROM Student WHERE student_id = $1", student_id
        )
        if deleted == "DELETE 0":
            raise HTTPException(status_code=404, detail="Студент не найден")
        return {"message": "Студент удалён"}


# Роуты для учителей
@app.get("/teachers", response_model=List[Teacher])
async def get_teachers():
    """
    Создать новый курс
    GET /teachers
    Accept: application/json
    """
    async with db_manager as manager:
        teachers = await manager.fetch(
            "SELECT * FROM Teacher"
        )
        return [Teacher(**teacher) for teacher in teachers]


# Роуты для курсов
@app.post("/courses", response_model=Course)
async def create_course(course: CourseCreate):
    """
    Создать новый курс
    POST /courses
    Content-Type: application/json

    Ожидаемые параметры:
    {
      "course_name": str,  // Название курса
      "department_id": int  // Идентификатор кафедры
    }
    """
    async with db_manager as manager:
        course_id = await manager.fetchval(
            "INSERT INTO Course (course_name, department_id) VALUES ($1, $2) RETURNING course_id",
            course.course_name, course.department_id
        )
        return {**course.dict(), "course_id": course_id}


@app.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int):
    """
    Получить информацию о курсе по его id
    GET /courses/{course_id}
    Accept: application/json

    Параметры:
    course_id - идентификатор курса (целое число)
    """
    async with db_manager as manager:
        course = await manager.fetchrow(
            "SELECT * FROM Course WHERE course_id = $1", course_id
        )
        if course is None:
            raise HTTPException(status_code=404, detail="Курс не найден")
        return Course(**course)


@app.get("/courses/{course_id}/students", response_model=List[Student])
async def get_course_students(course_id: int):
    """
    Получить список всех студентов на курсе
    GET /courses/{course_id}/students
    Accept: application/json

    Параметры:
    course_id - идентификатор курса (целое число)
    """
    async with db_manager as manager:
        students = await manager.fetch(
            "SELECT * FROM Student WHERE class_id IN (SELECT class_id FROM Class WHERE course_id = $1)",
            course_id
        )
        return [Student(**student) for student in students]


# Роуты для оценок
@app.post("/grades", response_model=Grade)
async def create_grade(grade: GradeCreate):
    """
    Создать новую оценку для студента по курсу
    POST /grades
    Content-Type: application/json

    Ожидаемые параметры:
    {
      "grade_value": int,  // Значение оценки
      "student_id": int,  // Идентификатор студента
      "class_id": int  // Идентификатор курса
    }
    """
    async with db_manager as manager:
        grade_id = await manager.fetchval(
            "INSERT INTO Grade (grade_value, student_id, class_id) VALUES ($1, $2, $3) RETURNING grade_id",
            grade.grade_value, grade.student_id, grade.class_id
        )
        return {**grade.dict(), "grade_id": grade_id}


@app.put("/grades/{grade_id}", response_model=Grade)
async def update_grade(grade_id: int, grade: GradeCreate):
    """
    Обновить оценку студента по курсу
    PUT /grades/{grade_id}
    Content-Type: application/json

    Ожидаемые параметры:
    {
      "grade_value": int,  // Значение оценки
      "student_id": int,  // Идентификатор студента
      "class_id": int  // Идентификатор курса
    }

    Параметры:
    grade_id - идентификатор оценки (целое число)
    """
    async with db_manager as manager:
        updated_grade = await manager.fetchrow(
            "UPDATE Grade SET grade_value = $1, student_id = $2, class_id = $3 WHERE grade_id = $4 RETURNING *",
            grade.grade_value, grade.student_id, grade.class_id, grade_id
        )
        if updated_grade is None:
            raise HTTPException(status_code=404, detail="Оценка не найдена")
        return Grade(**updated_grade)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
