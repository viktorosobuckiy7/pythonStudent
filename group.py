from student import Student
from config import STUDENT_LIMIT_IN_GROUP


class ExceptionStudentGroup(Exception):
    pass


class Group:

    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)
        if len(self.students) > STUDENT_LIMIT_IN_GROUP:
            raise ExceptionStudentGroup("Cлишком много студентов в группе")

    def del_student(self,student: Student):
        if student  in self.students:
            self.students.remove()

    def search_by_surname(self, value):
        res = [stud for stud in self.students if stud.last_name == value]
        return  res or None

    def __str__(self):
        return "\n".join(map(str,self.students))



