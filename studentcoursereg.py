from studentcourserepository import *

def student_course_registration():
    student_id = input('What is the student ID? ')
    course_id = input('What is the course ID? ')

    
    studentcourse_table_create()
    studentcourse_table_insert(student_id,course_id)

def delete_student_registration():
    student_id = input('Enter the students id: ')
    course_id = input('Enter the courses id: ')
    remove = input('Do you want to proceed?Y/N ')

    if remove == 'Y':
        studentcourse_table_delete(student_id, course_id)
        print('Operation completed')

    elif remove == 'N':
        print ('Operation canceled')
    
    else:
        print ('Invalid option')


def consult_studentcourses():
    student_courses = studentcourse_table_consult()
    for x in student_courses:
        print (x)

def consult_student_specific_courses():
    student_id = input('What is the student ID? ')

    coursetable = studentcourse_table_consult_student_id(student_id)
    for x in coursetable:
        print(x)

def consult_course_specific_students():
    course_id = input('What is the course ID? ')

    studenttable = studentcourse_table_consult_course_id(course_id)
    for x in studenttable:
        print (x)