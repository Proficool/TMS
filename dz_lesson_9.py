class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name  # Имя человека
        self.age = age    # Возраст человека
        self.gender = gender  # Пол человека
    def __str__(self):
        return f"{self.name}, {self.age} лет, {self.gender}"

class Student(Person):  # Наследование
    def __init__(self, name: str, age: int, gender: str, student_id: str, grades: list[float]): 
        super().__init__(name, age, gender)  # Наследование: вызов конструктора базового класса
        self.student_id = student_id  # Номер зачетной книжки
        self.__grades = grades  # Инкапсуляция: защищенное поле для хранения оценок

    def get_average_grade(self) -> float:
        #Рассчитывает средний балл студента
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0.0

    def __str__(self):  # Полиморфизм
        avg_grade = self.get_average_grade()
        return f"Студент: {self.name}, {self.age} лет, {self.gender}, ID: {self.student_id}, средний балл: {avg_grade:.2f}"

class Group:
    def __init__(self, group_name: str):
        self.group_name = group_name  # Название группы
        self.__students = []  # Инкапсуляция: защищенный список студентов

    def add_student(self, student: Student):
        self.__students.append(student) # Добавляет студента в группу

    def remove_student(self, student_id: str):
        """Удаляет студента по ID зачетной книжки из группы."""
        self.__students = [student for student in self.__students if student.student_id != student_id]

    def get_average_group_grade(self) -> float: #Рассчитывает средний балл всех студентов в группе
        if not self.__students:
            return 0.0
        return sum(student.get_average_grade() for student in self.__students) / len(self.__students)

    def list_students(self): #Выводит список всех студентов в группе
        print(f"Список студентов группы '{self.group_name}':")
        for student in self.__students:
            print(student)  # Полиморфизм: вызов переопределенного метода __str__ у Student
    def __str__(self):
        return f"Группа '{self.group_name}', всего студентов: {len(self.__students)}"

    # Создание студентов
student1 = Student(name="Иван", age=19, gender="мужской", student_id="S001", grades=[5, 4, 5])
student2 = Student(name="Мария", age=20, gender="женский", student_id="S002", grades=[3, 4, 5])
student3 = Student(name="Сергей", age=18, gender="мужской", student_id="S003", grades=[4, 4, 4])
student4 = Student(name="Анна", age=21, gender="женский", student_id="S003", grades=[3, 5, 4])

    # Создание группы
group = Group(group_name="ФизМат-2024")

    # Добавление студентов
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.add_student(student4)

    # Вывод списка студентов
group.list_students()

    # Средний балл по группе
print(f"\nСредний балл по группе: {group.get_average_group_grade():.2f}")

    # Удаление студента
group.remove_student("S002")
print("\nПосле удаления студента:")
group.list_students()