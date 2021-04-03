import uuid
from studentrepository import *
 

def student_info():
    student_id = uuid.uuid4().hex[:8]
    name = input('Student Name: ')
    lastname = input('Lastname: ')
    birth = input('Birthdate(YYYY-MM-DD): ')
    major =  input('Major: ')

    student_table_create()
    student_table_insert(student_id, name, lastname, birth, major)
    

def update_student():
    student_id = input('Enter the student ID of the student you wish to update: ')
    student = student_table_get_student(student_id)
    print (student) 

    # Get student info #

    name = input('Name: ') or student[0][1]
    lastname = input('Lastname: ') or student[0][2]
    birthdate = input('Birthdate: ') or student[0][3]
    major = input('Major: ') or student[0][4]
    student_table_update_student(student_id, name, lastname, birthdate, major)
    print ('Changes made succesfully')
    
def remove_student():
    student_id = input('Enter the ID of the student you wish to remove: ')
    student = student_table_get_student(student_id)
    if len(student) == 0:
        print ('Student not found')
    else:
        print (student)
        remove = input('Do you wish to proceed?Y/N ')
        if remove == 'Y':
            student_table_delete_student(student_id)
        elif remove == 'N':
            print ('Operation canceled')
        else:
            print ('Invalid option')

def consult_student():
    students = student_table_consult()
    for x in students:
        print (x)