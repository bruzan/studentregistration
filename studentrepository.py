import mysql.connector

db = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'students'
)

cursor = db.cursor()

def student_table_create():
    cursor.execute('CREATE TABLE IF NOT EXISTS students (student_id VARCHAR(8) PRIMARY KEY NOT NULL, name VARCHAR(30) NOT NULL, lastname VARCHAR(30) NOT NULL, birthdate DATE, major VARCHAR(30))')

def student_table_insert(student_id, name, lastname, birth, major):
    insert = ('INSERT INTO students (student_id, name, lastname, birthdate, major) VALUES (%s, %s, %s, %s, %s)')
    values = (student_id, name, lastname, birth, major)
    cursor.execute (insert, values)
    db.commit()

def student_table_consult():
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    return result



def student_table_get_student(student_id):
    sql = 'SELECT * FROM students WHERE student_id = %s'
    value = (student_id,)
    cursor.execute(sql, value)
    result = cursor.fetchall()
    return result
    

def student_table_update_student(student_id, name, lastname, birthdate, major):
    sql2 = 'UPDATE students SET name = %s, lastname = %s, birthdate = %s, major = %s WHERE student_id = %s'
    values2 = (name, lastname, birthdate, major, student_id)
    cursor.execute(sql2, values2)
    db.commit()


def student_table_delete_student(student_id):
    sql = 'DELETE FROM students WHERE student_id = %s'
    val = (student_id,)
    cursor.execute(sql,val)
    db.commit()
    print ('Student removed')