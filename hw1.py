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
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
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