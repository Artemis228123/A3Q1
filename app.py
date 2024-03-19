import psycopg2

# Use your own info here
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="school", 
        user="postgres",
        password="password"
    )
    return conn

def getAllStudents():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    print("All students:")
    for row in rows:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
        """, 
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Student added successfully")

def updateStudentEmail(student_id, new_email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET email = %s
        WHERE student_id = %s
        """,
        (new_email, student_id) 
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Student email updated successfully")

def deleteStudent(student_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM students 
        WHERE student_id = %s
        """,
        (student_id,)
    )
    conn.commit()
    cur.close() 
    conn.close()
    print("Student deleted successfully")

# Example usage with user input prompts
input("Press Enter to get all students...")
getAllStudents()

input("\nPress Enter to add a new student...")
addStudent('Alice', 'Wonderland', 'alice@example.com', '2023-09-03')
getAllStudents()

input("\nPress Enter to update a student's email...")
updateStudentEmail(2, 'janesmith@example.com') 
getAllStudents()

input("\nPress Enter to delete a student...")
deleteStudent(4)
getAllStudents()