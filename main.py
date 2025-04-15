from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

# Adding School
school = School('ABC', 'Dhaka')


# Adding Classrooms
eight = Classroom('Eight')
nine = Classroom('Nine')
ten = Classroom('Ten')
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)



# Adding Students
rahim = Student('Rahim', eight)
karim = Student('karim', nine)
fahim = Student('fahim', ten)
hamim = Student('hamim', ten)
school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)




# Adding Students
t1 = Teacher('Mr 1')
t2 = Teacher('Mr 2')
t3 = Teacher('Mr 3')
t4 = Teacher('Mr 4')



# Adding Subjects
bangla = Subject('Bangla', t1)
physics = Subject('Physics', t2)
chemistry = Subject('Chemistry', t3)
biology = Subject('Biology', t4)

eight.add_subjects(bangla)
eight.add_subjects(physics)
eight.add_subjects(chemistry)
nine.add_subjects(bangla)
nine.add_subjects(biology)
ten.add_subjects(biology)
ten.add_subjects(bangla)
ten.add_subjects(physics)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)