class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_students(student)

    @staticmethod
    def calc_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A'
        elif marks>=60 and marks<70:
            return 'A-'
        elif marks>=50 and marks<60:
            return 'B'
        elif marks>=40 and marks<50:
            return 'C'
        elif marks>=33 and marks<40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_gpa(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00,
        }
        return grade_map[grade]
    
    @staticmethod
    def gpa_to_grade(gpa):
        if gpa >= 5:
            return 'A+'
        elif gpa>=4 and gpa<5:
            return 'A'
        elif gpa>=3.5 and gpa<4:
            return 'A-'
        elif gpa>=3 and gpa<3.5:
            return 'B'
        elif gpa>=2 and gpa<3:
            return 'C'
        elif gpa>=1 and gpa<2:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self):
        # all classrooms
        print('\n----(All Classes)----')
        for key in self.classrooms.keys():
            print(key)

        # all students
        print('\n----(All Students)----')
        result = ''
        for key, value in self.classrooms.items():
            result += f'---{key.upper()} Classroom Students\n'
            for student in value.students:
                result += f'{student.name}\n'
        print(result)

        # all subjects
        subject = ''
        for key, value in self.classrooms.items():
            subject += f'---{key.upper()} Classroom Subjects\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject)

        # all teachers



        # all student's result
        print('----------(Students Results)----------')
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.final_grade())
        return ''