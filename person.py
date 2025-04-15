import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name








class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1,100)
    







class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}             # {'eng': 78, ...}
        self.subject_grade = {}     # {'eng': 'A', ...}
        self.grade = None           # final grade

    def final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_gpa(grade)
            sum += point
        gpa = sum/len(self.subject_grade)
        self.grade = School.gpa_to_grade(gpa)
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
