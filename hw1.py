class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Метод rate_hw должен быть присвоен только дочернему классу reviewer и убран из mentor
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def lectures(self, course, topic):
        if course not in self.courses_attached:
            return f"Курс '{course}' не закреплен за лектором {self.name} {self.surname}."
        print(f"{self.name} {self.surname} прочитал лекцию по теме '{topic}' на курсе '{course}'.")

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews_count = 0

    def rate_hw(self, student, course, grade):
        result = super().rate_hw(student, course, grade)
        if result != 'Ошибка':
            self.reviews_count += 1
        return result

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')

print(isinstance(lecturer, Mentor))      # True
print(isinstance(reviewer, Mentor))      # True
print(lecturer.courses_attached)         # []
print(reviewer.courses_attached)         # []