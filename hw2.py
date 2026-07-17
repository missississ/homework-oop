class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def rate_hw(self, student, course, grade):
        return "Ошибка! Лектор не может выставлять оценки"
    
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
    
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return "Ошибка"
        if course not in lecturer.courses_attached:
            return "Ошибка"
        if course not in self.courses_in_progress:
                return 'Ошибка'
        if not (0 <= grade <= 10):
            return 'Ошибка: оценка должна быть от 0 до 10'

        lecturer.grades.setdefault(course, []).append(grade)
        return None
 
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}  