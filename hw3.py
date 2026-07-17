class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

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

    def avg_lecture_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)

        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecture_grade() == other.avg_lecture_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecture_grade() < other.avg_lecture_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecture_grade() > other.avg_lecture_grade()
    
    def __str__(self):
        avg = self.avg_lecture_grade()
        return f"Имя {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg:.1f} "
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviews_count = 0

    def rate_hw(self, student, course, grade):
        result = super().rate_hw(student, course, grade)
        if result != 'Ошибка':
            self.reviews_count += 1
        return result
    def __str__(self):
        return f"Имя {self.name}\nФамилия: {self.surname}"
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
    
    def avg_hw_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_hw_grade() == other.avg_hw_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_hw_grade() < other.avg_hw_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_hw_grade() > other.avg_hw_grade()
    
    def __str__(self):
        avg = self.avg_hw_grade()
        self.courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        self.finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет"

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg:.1f}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress_str}\n"
                f"Завершенные курсы: {self.finished_courses_str}")

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Татьяна', 'Климова', 'Ж')

student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
lecturer.courses_attached += ['Python']
reviewer.courses_attached += ['Python']

student.grades['Python'] = [10, 9.7, 10]

lecturer.grades['Python'] = [10, 9.7, 10]

lecturer2 = Lecturer('Анна', 'Смирнова')
lecturer2.courses_attached += ['Python']
lecturer2.grades['Python'] = [8, 8, 10]

student2 = Student('Мария', 'Белова', 'Ж')
student2.courses_in_progress += ['Python']
student2.grades['Python'] = [7, 8, 8]

# Проверка для задания 3.1
print("--- Вывод проверяющих ---")
print(reviewer)

print("\n--- Вывод лекторов ---")
print(lecturer)

print("\n--- Вывод студентов ---")
print(student)

# Проверка для задания 3.2
print("--- Сравнение лекторов ---")
print(lecturer == lecturer2)
print(lecturer < lecturer2)
print(lecturer > lecturer2)

print("\n--- Сравнение студентов ---")
print(student == student2)
print(student < student2)
print(student > student2)
