import random
import os

courses = []

class Course:
    # class variables
    semester = 'Fall 2025'

    def __init__(self, name='', categories=None):

        self.section = random.randint(10000, 100000)
        self.name = name
        self.student_count = 0
        self.class_roster = []

        if categories is None:
            self.categories = {}
            self.enter_categories()
        else: self.categories = categories

    def change_semester(clear, semester):
        clear.semester = semester

    def enter_categories(self):

        more_categories = 'y'
        while more_categories == 'y':
            print(f'Enter grading categories for {self.name}')
            category = input('5 letter max Category name: ')
            total = input(f'Enter total points for that {category}')
            self.categories[category] = int(total)
            more_categories = input('\nDo you have more categories to enter (Y/N): ').casefold()

            os.system('clear')

    def enroll_students(self,number):

        self.student_count += number
        for n in range(number):
            temp_student = Student(self.categories)
            temp_student.fullname = input('Enter student first and last name: ')
            temp_student.enter_scores()
            self.class_roster.append(temp_student)

    def __str__(self):

        message = f'Course {self.section} - {self.name} has {self.student_count} students:\n'
        for stu in self.class_roster:
            message += f'{stu} - '
            for cat in self.categories:
                message += f'{cat}: {stu.scores[cat]}/{self.categories[cat]}, '
            message += '\n'
        return message

class Student:

    def __init__(self, categories, fname='Jane', lname='Doe'):
        self.first = fname.capitalize()
        self.last = lname.capitalize()
        self.scores = {}
        for key in categories:
            self.scores[key] = 0

    def fullname(self):
        return f'{self.last}, {self.first}'

    def fullname(self, name):
        try:
            self.first, self.last = name.split(' ')
        except ValueError:
            pass

    def __str__(self):
        return self.fullname

    def enter_scores(self):
        for category in self.scores:
            score = int(input(f'Enter earned points for {category}: '))
            self.scores[category] = score

print(f"{'University System' :*^30}")
Course.change_semester(input('Enter semester and year for which you are creating courses: '))

enter_courses = 'y'
print("\nEntering course information")
while enter_courses == 'y' :
    course_name = input('Enter course name: ').upper()
    new_course = Course(course_name)
    courses.append(new_course)
    enter_courses = input("\nAdd another course (Y/N)? ").casefold()

os.system('clear')
for c in courses:
    print(f'\nAdd students to {c.name} course')
    numberOfStudents = int(input('How many students to you want to enroll? '))
    c.enroll_students(numberOfStudents)

os.system('clear')
print(f'\nCourse Information for {Course.semester}')
for c in courses:
    print(c)