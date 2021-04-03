from studentreg import *
from coursereg import *
from studentcoursereg import *



def menu():
    print ('What would you like to do?')
    print ('Type 1 to register a new student')
    print ('Type 2 to register a new course')
    print ('Type 3 to update a students information')
    print ('Type 4 to update a courses information')
    print ('Type 5 to remove a students registration')
    print ('Type 6 to remove a courses registration')
    print ('Type 7 to consult the students registration')
    print ('Type 8 to consult the courses registration')
    print ('Type 9 to register a student in a course')
    print ('Type 10 to consult all students registered in all courses')
    print ('Type 11 to consult all courses a specific student is registered in')
    print ('Type 12 to consult all students registered in a specific course')
    print ('Type 13 to remove a students registration from a course')
    print ('Type 99 to exit')
    
    
while True:
    menu()
    option=int(input())

    if option == 1:
        student_info()

    elif option == 2:
        course_info()

    elif option == 3:
        update_student()

    elif option == 4:
        course_update()

    elif option == 5:
        remove_student()

    elif option == 6:
        remove_course()

    elif option == 7:
        consult_student()

    elif option == 8:
        consult_course()

    elif option == 9:
        student_course_registration()

    elif option == 10:
        consult_studentcourses()

    elif option == 11:
        consult_student_specific_courses()

    elif option == 12:
        consult_course_specific_students()

    elif option == 13:
        delete_student_registration()

    elif option == 99:
        break
    
    else:
        print ('Invalid option')



    
