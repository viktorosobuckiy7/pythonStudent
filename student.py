from person import Person


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)


    def __str__(self):
        return f"Имя студента - {self.first_name}," \
               f" фамилия - {self.last_name}, " \
               f" возраст - {self.age},"



