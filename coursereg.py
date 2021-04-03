import uuid
from courserepository import *

def course_info():
    course_id = uuid.uuid4().hex[:8]
    name = input('Course name? ')
    start = input('Course start: ')
    end = input('Course end: ')

    course_table_create()
    course_table_insert(course_id, name, start, end)

def course_update():
    course_id = input('Enter the course id of the course you wish to update: ')
    course = course_table_get_course(course_id)
    print (course)

    ## Update course info ##

    name = input('New course name: ') or course[0][1]
    start = input('New course start date(YYYY-MM-DD): ') or course[0][2]
    end = input('New course end date(YYYY-MM-DD): ') or course[0][3]
    course_table_update_course(course_id, name, start, end)
    print ('Changes made succesfully')

def remove_course():
    course_id = input('Enter the ID of the course you wish to remove: ')
    course = course_table_get_course(course_id)
    if len(course) == 0:
        print ('Course not found')
    else:
        print (course)
        remove = input('Do you wish to proceed?Y/N ')
        if remove == 'Y':
            course_table_delete_course(course_id)
        elif remove == 'N':
            print ('Operation canceled')
        else:
            print ('Invalid option')

def consult_course():
    courses = course_table_consult()
    for x in courses:
        print (x)