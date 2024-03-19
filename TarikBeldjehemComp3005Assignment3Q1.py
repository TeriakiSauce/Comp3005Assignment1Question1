import psycopg2

# Tarik Beldjehem 101187965 Comp 3005 Assignment 3 Question 1

# Connect to Database using host, user, password, port and database name parameters
conct = psycopg2.connect(host="localhost", user="user1", password ="1234", port=5432, dbname="Assignment_3_Q_1")
cursr = conct.cursor()

def getAllStudents():
    """
    Retrieves and displays all records from the students table
    """
    print('students:')
    cursr.execute("""SELECT * FROM students""")
    for row in cursr.fetchall():
        print(row)
    print("\n")

def addStudent(first_name, last_name, email, enrollment_date):
    """Adds a new student to the students table

    Args:
        first_name (str): the student's first name
        last_name (str): the student's last name
        email (str): the student's email
        enrollment_date (str): the student's date of enrollment
    """
    parameters = (first_name, last_name, email, enrollment_date)
    statement = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"""
    cursr.execute(statement, parameters)
    print("\n")
    
def updateEmail(student_id, new_email):
    """Updates the email of a student in the students table

    Args:
        student_id (str): the student id of the student to be modified
        new_email (str): the new email that will overwrite the old student email
    """
    parameters = (new_email, student_id)
    statement = """UPDATE students SET email = %s WHERE student_id = %s"""
    cursr.execute(statement, parameters)
    print("\n")
    
def deleteStudent(student_id):
    """Deletes a student with the specified student id in the students table

    Args:
        student_id (str): the student id of the student to be removed
    """
    parameters = (student_id,)
    statement = """DELETE FROM students WHERE student_id = %s"""
    cursr.execute(statement, parameters)
    print("\n")

commands = ""
print("Enter a number to execute a command for the students table")
while(commands!= "q"):
    print("""Possible commands are:\n
          1. getAllStudents()\n
          2. addStudent()\n
          3. updateEmail()\n
          4. deleteStudent()\n
          q (to quit)\n""")
    commands = input("Enter a command:")
    if (commands == "1"):
        getAllStudents()
        
    elif (commands == "2"):
        first_name = input("Enter their first name:")
        last_name = input("Enter their last name:")
        email = input("Enter their email:")
        enrollment_date = input("Enter their enrollment date:")
        addStudent(first_name, last_name, email, enrollment_date)
        
    elif (commands == "3"):
        student_id = input("Enter their student id:")
        new_email = input("Enter their new email:")
        updateEmail(student_id, new_email)
        
    elif (commands == "4"):
        student_id = input("Enter their student id:")
        deleteStudent(student_id)
      
conct.commit()
cursr.close()
conct.close()