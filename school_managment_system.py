import mysql.connector

def connect_db():
    """Connect to MySQL and initialize database & tables"""
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="#green368!")
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pyschool")
        cursor.execute("USE pyschool")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pystudent(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                _class VARCHAR(25) NOT NULL,
                roll_number VARCHAR(25) UNIQUE,
                gender ENUM('M','F')
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pystaff(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                gender ENUM('M','F'),
                subject VARCHAR(25) NOT NULL,
                salary INT
            )
        """)
        mydb.commit()
        print(" ******** SCHOOL MANAGEMENT SYSTEM ******** ")
        print(" Successfully connected to database ")
        return mydb, cursor
    except Exception as e:
        print("Error connecting to database:", e)
        exit()

# Add Student
def add_student(cursor, mydb):
    print(" All information prompted are mandatory to be filled ")
    name = input(" Enter name (limit upto 35 characters): ")
    class_name = input(" Enter Class: ")
    roll_number = input(" Enter the roll number: ")
    gender = input(" Enter Gender (M/F): ").upper()

    query = "INSERT INTO pystudent (name, _class, roll_number, gender) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, class_name, roll_number, gender))
    mydb.commit()
    print(" Student record has been saved successfully !! ")

# Add Staff
def add_staff(cursor, mydb):
    print(" All information prompted are mandatory to be filled ")
    name = input(" Enter staff member name (limit upto 35 characters): ")
    gender = input(" Enter Gender (M/F): ").upper()
    dep = input(" Enter subject or department: ")
    salary = int(input(" Enter the Salary: "))

    query = "INSERT INTO pystaff (name, gender, subject, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, gender, dep, salary))
    mydb.commit()
    print(" Staff record has been saved successfully !! ")

# Search Student
def search_student(cursor):
    roll_number = input(" Enter student roll_number: ")
    query = "SELECT name, _class, roll_number, gender FROM pystudent WHERE roll_number = %s"
    cursor.execute(query, (roll_number,))
    result = cursor.fetchone()
    if result:
        name, class_name, roll, gender = result
        print(f"Name:- {name}\nClass:- {class_name}\nRoll Number:- {roll}\nGender:- {gender}")
    else:
        print(" No student found with that roll number.")

# Search Staff
def search_staff(cursor):
    name = input(" Enter staff name: ")
    query = "SELECT name, gender, subject, salary FROM pystaff WHERE name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    if result:
        name, gender, dep, salary = result
        print(f"Name:- {name}\nGender:- {gender}\nDepartment:- {dep}\nSalary:- {salary}")
    else:
        print(" No staff member found with that name.")

# Delete Student
def delete_student(cursor, mydb):
    roll_number = input(" Enter roll_number: ")
    query = "DELETE FROM pystudent WHERE roll_number = %s"
    cursor.execute(query, (roll_number,))
    mydb.commit()
    if cursor.rowcount > 0:
        print(" Student Record is successfully deleted ")
    else:
        print(" No record found to delete.")

# Delete Staff
def delete_staff(cursor, mydb):
    name = input(" Enter staff member name: ")
    query = "DELETE FROM pystaff WHERE name = %s"
    cursor.execute(query, (name,))
    mydb.commit()
    if cursor.rowcount > 0:
        print(" Staff Record is successfully deleted ")
    else:
        print(" No record found to delete.")

# Main Menu
def main():
    mydb, cursor = connect_db()
    while True:
        print("\n PLEASE TYPE THE FOLLOWING NUMBERS FOR THE RESPECTIVE TASK NEEDED TO BE PERFORMED :: ")
        print(" 1 = Enter Data for new student ")
        print(" 2 = Enter Data for new staff member ")
        print(" 3 = Search Student Data ")
        print(" 4 = Search Staff Data ")
        print(" 5 = Remove Student Record ")
        print(" 6 = Remove Staff record ")
        print(" 7 = Exit ")

        try:
            ch = int(input(" Enter your choice: "))
        except ValueError:
            print(" Invalid input! Please enter a number.")
            continue

        if ch == 1:
            add_student(cursor, mydb)
        elif ch == 2:
            add_staff(cursor, mydb)
        elif ch == 3:
            search_student(cursor)
        elif ch == 4:
            search_staff(cursor)
        elif ch == 5:
            delete_student(cursor, mydb)
        elif ch == 6:
            delete_staff(cursor, mydb)
        elif ch == 7:
            print(" Exiting... Thank you for using the system. ")
            break
        else:
            print(" Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
