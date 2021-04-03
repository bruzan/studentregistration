import mysql.connector

db = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'root',
database = 'students'
)

cursor = db.cursor()

def course_table_create():
    cursor.execute('CREATE TABLE IF NOT EXISTS courses (course_id VARCHAR(8) PRIMARY KEY NOT NULL, name VARCHAR(30) NOT NULL, start DATE, end DATE)')
    db.commit()

def course_table_insert(course_id, name, start, end):
    insert = ('INSERT INTO courses (course_id, name, start, end) VALUES (%s, %s, %s, %s)')
    values = (course_id, name, start, end)
    cursor.execute(insert, values)
    db.commit()

def course_table_consult():
    cursor.execute('SELECT * FROM courses')
    result = cursor.fetchall()
    return result

def course_table_get_course(course_id):
    sql = 'SELECT * FROM courses WHERE course_id = %s'
    value = (course_id,)
    cursor.execute(sql, value)
    result = cursor.fetchall()
    return result

def course_table_update_course(course_id, name, start, end):
    sql2 = 'UPDATE courses SET name = %s, start = %s, end = %s WHERE course_id = %s'
    values2 = (name, start, end, course_id)
    cursor.execute(sql2, values2)
    db.commit()

def course_table_delete_course(course_id):
    sql = 'DELETE FROM courses WHERE course_id = %s'
    val = (course_id,)
    cursor.execute(sql,val)
    db.commit()
    print ('Course removed')
