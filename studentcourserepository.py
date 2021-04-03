import mysql.connector

db = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'students'
)

cursor = db.cursor()

def studentcourse_table_create():
    cursor.execute('CREATE TABLE IF NOT EXISTS student_courses (student_id VARCHAR(8)  NOT NULL, course_id VARCHAR(8) NOT NULL, FOREIGN KEY (student_id) REFERENCES students(student_id), FOREIGN KEY (course_id) REFERENCES courses(course_id), PRIMARY KEY(student_id, course_id))')
    db.commit()

def studentcourse_table_insert(student_id,course_id):
    sql = ('INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s)')
    values = (student_id, course_id)
    cursor.execute(sql, values)
    db.commit()

def studentcourse_table_delete(student_id,course_id):
    sql = 'DELETE FROM student_courses WHERE student_id = %s and course_id = %s'
    val = (student_id, course_id)
    cursor.execute(sql,val)
    db.commit()

def studentcourse_table_consult():
    sql = 'SELECT students.name, students.lastname, courses.name FROM students INNER JOIN student_courses on students.student_id = student_courses.student_id INNER JOIN courses on courses.course_id = student_courses.course_id'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def studentcourse_table_consult_student_id(student_id):
    sql = 'SELECT students.name, students.lastname, courses.name FROM students INNER JOIN student_courses on students.student_id = student_courses.student_id INNER JOIN courses on courses.course_id = student_courses.course_id WHERE students.student_id = %s'
    val = (student_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    return result

def studentcourse_table_consult_course_id(course_id):
    sql = 'SELECT students.name, students.lastname, courses.name FROM students INNER JOIN student_courses on students.student_id = student_courses.student_id INNER JOIN courses on courses.course_id = student_courses.course_id WHERE courses.course_id = %s'
    val = (course_id,)
    cursor.execute(sql,val)
    result = cursor.fetchall()
    return result

    



