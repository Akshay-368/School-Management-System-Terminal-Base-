# School Management System (Terminal-Based)

A robust terminal-based School Management System built with Python and MySQL. This project allows easy management of student and staff records through a simple CLI interface.

## Features & Strengths

- **Database Integration**: Uses MySQL for persistent storage. The system creates necessary databases and tables automatically upon first run.
- **Student & Staff Management**: Easily add, search, and delete records for students and staff members.
- **Input Validation & Error Handling**: Basic input validation and helpful error messages guide users and prevent crashes.
- **Modular Design**: Functions for each operation make the code easy to read, maintain, and extend.
- **CLI-based Interaction**: All operations are handled via terminal prompts, making it lightweight and easy to use without a GUI.

## Key Techniques

- **Python-MySQL Integration**: Utilizes `mysql.connector` for seamless database operations.
- **Dynamic Table Creation**: Ensures tables and database are present before transactions.
- **SQL Parameterization**: Prevents SQL injection and ensures safe data handling.
- **Menu-Driven Interface**: Clear command-line menu for user-friendly operation.

## Key Learnings

- **Database Schema Design**: Structuring tables for school data, including unique constraints and ENUM fields for gender.
- **Error Handling**: Anticipating and managing database connection issues and validation errors.
- **CRUD Operations**: Implementing Create, Read, Update, and Delete logic for records.
- **User Experience**: Designing effective CLI prompts and feedback messages for smooth operation.

## Setup Instructions

1. **Install MySQL Server**  
   Ensure MySQL is installed and running on your machine.

2. **Install Python Dependencies**  
   ```bash
   pip install mysql-connector-python
   ```

3. **Configure Database Credentials**  
   Update `host`, `user`, and `passwd` in `school_management_system.py` if needed.

4. **Run the Application**  
   ```bash
   python school_management_system.py
   ```

5. **Follow Menu Prompts**  
   Add, search, or delete student/staff records as required.

## Example Usage

```bash
$ python school_management_system.py
 ******** SCHOOL MANAGEMENT SYSTEM ******** 
 Successfully connected to database 
 PLEASE TYPE THE FOLLOWING NUMBERS FOR THE RESPECTIVE TASK NEEDED TO BE PERFORMED ::
 1 = Enter Data for new student
 2 = Enter Data for new staff member
 3 = Search Student Data
 4 = Search Staff Data
 5 = Remove Student Record
 6 = Remove Staff record
 7 = Exit
```

## Strengths

- **Ease of Use**: Simple and direct interaction for managing records.
- **Extensibility**: Modular code can be adapted for more features (attendance, grading, etc.).
- **Reliability**: Database-backed system ensures data is persistent and reliable.

## License

MIT License

---

*Happy Learning & Building!*