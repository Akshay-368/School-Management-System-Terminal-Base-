import mysql.connector

def connect_db():
    """Connect to MySQL and initialize database & tables"""
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="#green368!")
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pyschool")
        cursor.execute("USE pyschool")

        # Students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pystudent(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                _class VARCHAR(25) NOT NULL,
                roll_number VARCHAR(25) UNIQUE,
                gender ENUM('M','F')
            )
        """)

        # Staff table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pystaff(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                gender ENUM('M','F'),
                subject VARCHAR(25) NOT NULL,
                salary INT
            )
        """)

        # Users table for login & roles
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                role ENUM('admin','staff','student') NOT NULL
            )
        """)

        mydb.commit()
        print(" ******** SCHOOL MANAGEMENT SYSTEM ******** ")
        print(" Successfully connected to database ")
        return mydb, cursor

    except Exception as e:
        print("Error connecting to database:", e)
        exit()


# --- CRUD Operations ---
def add_student(cursor, mydb):
    name = input("Enter student name: ")
    class_name = input("Enter class: ")
    roll_number = input("Enter roll number: ")
    gender = input("Enter Gender (M/F): ").upper()
    query = "INSERT INTO pystudent (name, _class, roll_number, gender) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, class_name, roll_number, gender))
    mydb.commit()
    print("Student record saved successfully!")


def add_staff(cursor, mydb):
    name = input("Enter staff name: ")
    gender = input("Enter Gender (M/F): ").upper()
    subject = input("Enter subject/department: ")
    salary = int(input("Enter salary: "))
    query = "INSERT INTO pystaff (name, gender, subject, salary) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, gender, subject, salary))
    mydb.commit()
    print("Staff record saved successfully!")


def search_student(cursor):
    roll_number = input("Enter student roll number: ")
    query = "SELECT name, _class, roll_number, gender FROM pystudent WHERE roll_number=%s"
    cursor.execute(query, (roll_number,))
    result = cursor.fetchone()
    if result:
        name, class_name, roll, gender = result
        print(f"Name: {name}\nClass: {class_name}\nRoll Number: {roll}\nGender: {gender}")
    else:
        print("No student found with that roll number.")


def search_staff(cursor):
    name = input("Enter staff name: ")
    query = "SELECT name, gender, subject, salary FROM pystaff WHERE name=%s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    if result:
        name, gender, subject, salary = result
        print(f"Name: {name}\nGender: {gender}\nSubject: {subject}\nSalary: {salary}")
    else:
        print("No staff member found with that name.")


def delete_student(cursor, mydb):
    roll_number = input("Enter student roll number to delete: ")
    query = "DELETE FROM pystudent WHERE roll_number=%s"
    cursor.execute(query, (roll_number,))
    mydb.commit()
    if cursor.rowcount > 0:
        print("Student record deleted successfully.")
    else:
        print("No record found to delete.")


def delete_staff(cursor, mydb):
    name = input("Enter staff name to delete: ")
    query = "DELETE FROM pystaff WHERE name=%s"
    cursor.execute(query, (name,))
    mydb.commit()
    if cursor.rowcount > 0:
        print("Staff record deleted successfully.")
    else:
        print("No record found to delete.")


# --- Role-based Login ---
def login(cursor):
    print("LOGIN")
    username = input("Username: ")
    password = input("Password: ")
    query = "SELECT role FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print(f"Login successful! Role: {result[0]}")
        return result[0]
    else:
        print("Invalid credentials! Exiting...")
        exit()


# --- Main Menu ---
def main():
    mydb, cursor = connect_db()
    role = login(cursor)

    while True:
        print("\n--- MENU ---")
        if role in ['admin', 'staff']:
            print("1 = Add Student")
        if role == 'admin':
            print("2 = Add Staff")
        print("3 = Search Student")
        if role in ['admin', 'staff']:
            print("4 = Search Staff")
        if role == 'admin':
            print("5 = Delete Student")
            print("6 = Delete Staff")
        print("7 = Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if ch == 1 and role in ['admin', 'staff']:
            add_student(cursor, mydb)
        elif ch == 2 and role == 'admin':
            add_staff(cursor, mydb)
        elif ch == 3:
            search_student(cursor)
        elif ch == 4 and role in ['admin', 'staff']:
            search_staff(cursor)
        elif ch == 5 and role == 'admin':
            delete_student(cursor, mydb)
        elif ch == 6 and role == 'admin':
            delete_staff(cursor, mydb)
        elif ch == 7:
            print("Exiting... Goodbye!")
            break
        else:
            print("You don't have permission to perform this action.")


if __name__ == "__main__":
    main()
