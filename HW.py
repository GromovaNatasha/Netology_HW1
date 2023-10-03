import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def mean_grade(self):
        grades = []
        for _, v in self.grades.items():
            grades += v
        if len(grades) == 0:
            return 0
        return statistics.mean(grades)
    
    def get_current_courses(self):
        return ', '.join(self.courses_in_progress)
    
    def get_finished_courses(self):
        return ', '.join(self.finished_courses)
        
    def rate_lecturer(self, lecturer, course, grade):
        if type(grade) != int or grade < 1 or grade > 10:
            return 'Оценка должна быть целым числом от 1 до 10'
        if (isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached):
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Средняя оценка за домашние задания: ' + str(self.mean_grade()) + '\n'
        result += 'Курсы в процессе изучения: ' + self.get_current_courses() + '\n'
        result += 'Завершенные курсы: ' + self.get_finished_courses()
        return result
    
    def __eq__(self, other):
        return self.mean_grade() == other.mean_grade()
    
    def __ne__(self, other):
        return self.mean_grade() != other.mean_grade()
    
    def __gt__(self, other):
        return self.mean_grade() > other.mean_grade()
    
    def __lt__(self, other):
        return self.mean_grade() < other.mean_grade()
    
    def __ge__(self, other):
        return self.mean_grade() <= other.mean_grade()
    
    def __le__(self, other):
        return self.mean_grade() >= other.mean_grade()
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        
    def mean_grade(self):
        grades = []
        for _, v in self.course_grades.items():
            grades += v
        if len(grades) == 0:
            return 0
        return statistics.mean(grades)
    
    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Средняя оценка за лекции: ' + str(self.mean_grade())
        return result
    
    def __eq__(self, other):
        return self.mean_grade() == other.mean_grade()
    
    def __ne__(self, other):
        return self.mean_grade() != other.mean_grade()
    
    def __gt__(self, other):
        return self.mean_grade() > other.mean_grade()
    
    def __lt__(self, other):
        return self.mean_grade() < other.mean_grade()
    
    def __ge__(self, other):
        return self.mean_grade() <= other.mean_grade()
    
    def __le__(self, other):
        return self.mean_grade() >= other.mean_grade()
         

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname
        return result
    
    
def mean_by_course_and_students(course, students):
    grades = []
    for student in students:
        if course in student.grades:
            grades += student.grades[course]
    if len(grades) == 0:
        return 0
    return statistics.mean(grades)

def mean_by_course_and_lectors(course, lectors):
    grades = []
    for lector in lectors:
        if course in lector.course_grades:
            grades += lector.course_grades[course]
    if len(grades) == 0:
        return 0
    return statistics.mean(grades)


        
lector_1 = Lecturer("Иван", "Петров")
lector_2 = Lecturer("Николай", "Иванов")

lector_1.courses_attached += ['Астропатия']
lector_2.courses_attached += ['Python']

reviewer_1 = Reviewer("Мария", "Козлова")
reviewer_2 = Reviewer("Сергей", "Клинов")

reviewer_1.courses_attached += ['Астропатия']
reviewer_2.courses_attached += ['Астропатия', 'Python']

student_1 = Student("Иван", "Руслов", "м")
student_2 = Student("Мария", "Пескова", "ж")

student_1.courses_in_progress += ['Астропатия', 'Python']
student_2.courses_in_progress += ['Python']

student_1.rate_lecturer(lector_1, "Астропатия", 8)
student_1.rate_lecturer(lector_2, "Python", 4)
student_2.rate_lecturer(lector_2, "Python", 7)

reviewer_1.rate_hw(student_1, 'Астропатия', 8)
reviewer_2.rate_hw(student_1, 'Астропатия', 7)

print('Студенты:')
print(student_1)
print('')
print(student_2)
print('')
print('Лекторы:')
print(lector_1)
print('')
print(lector_2)
print('')
print('Средние:')
print(mean_by_course_and_students('Астропатия', [student_1, student_2]))
print('')
print(mean_by_course_and_lectors('Астропатия', [lector_1, lector_2]))
print('')
print('Сравнение:')
print(lector_1 < lector_2)
print(student_1 < student_2)