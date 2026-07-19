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
        courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет"

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

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
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

            self.reviews_count += 1
            return None
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя {self.name}\nФамилия: {self.surname}"

def avg_student_grade_by_course(students, course):
    all_grades =[]
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])

    if not all_grades:
        return 0.0
    return sum(all_grades) / len(all_grades)

def avg_lecturer_grade_by_course(lecturers, course):
    all_grades =[]
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])

    if not all_grades:
        return 0.0
    return sum(all_grades) / len(all_grades)


lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Анна', 'Смирнова')

reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Алина', 'Петрова')

student1 = Student('Татьяна', 'Климова', 'Ж')
student2 = Student('Мария', 'Белова', 'Ж')

lecturer1.courses_attached += ['Python', 'Git']
lecturer2.courses_attached += ['Python']

reviewer1.courses_attached += ['Python', 'Git']
reviewer2.courses_attached += ['Python']

student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2.courses_in_progress += ['Python']
student2.finished_courses += ['HTML/CSS']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)

reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 9)

student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 9)

student2.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 10)

print("--- Вызов методов и вывод объектов ---")

lecturer1.lectures('Python', 'Основы синтаксиса')
lecturer1.lectures('Java', 'Попытка про Java')  # курс не прикреплён — будет сообщение об ошибке

print()
print(reviewer1)
print()
print(lecturer1)
print()
print(student1)

print("--- Сравнение лекторов ---")
print(lecturer1 == lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)

print("\n--- Сравнение студентов ---")
print(student1 == student2)
print(student1 < student2)
print(student1 > student2)

print("\n--- Средние по курсам ---")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_hw_python = avg_student_grade_by_course(students_list, 'Python')
print(f"Средняя оценка за ДЗ по Python: {avg_hw_python:.1f}")

avg_lect_python = avg_lecturer_grade_by_course(lecturers_list, 'Python')
print(f"Средняя оценка за лекции по Python: {avg_lect_python:.1f}")

avg_hw_git = avg_student_grade_by_course(students_list, 'Git')
print(f"Средняя оценка за ДЗ по Git: {avg_hw_git:.1f}")

avg_lect_git = avg_lecturer_grade_by_course(lecturers_list, 'Git')
print(f"Средняя оценка за лекции по Git: {avg_lect_git:.1f}")
