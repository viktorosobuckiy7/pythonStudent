class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.age = age

    def __str__(self):
        return f"Имя - {self.first_name}, Фамилия - {self.last_name}, возраст - {self.age}  "


