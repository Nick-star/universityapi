from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    class_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    course_name: str
    department_id: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int

    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    department_id: int

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    teacher_id: int

    class Config:
        orm_mode = True

class GradeBase(BaseModel):
    grade_value: int
    student_id: int
    class_id: int

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    grade_id: int

    class Config:
        orm_mode = True
