# School Management System (Terminal-Based)

A robust terminal-based School Management System built with Python and MySQL. This project allows easy management of student and staff records through a simple CLI interface.

## Features & Strengths

- **Database Integration**: Uses MySQL for persistent storage. The system creates necessary databases and tables automatically upon first run.
- **Student & Staff Management**: Easily add, search, and delete records for students and staff members.
- **Role-Based Login System**: Secure login for users (admin, staff, student) with permissions to restrict access to sensitive operations.
- **Permissions & Access Control**: Menu options and operations are enabled/disabled based on the logged-in user's role.
- **User Management**: Admins and staff log in via credentials stored in the database. The `users` table manages usernames, passwords, and roles.
- **Input Validation & Error Handling**: Basic input validation and helpful error messages guide users and prevent crashes.
- **Modular Design**: Functions for each operation make the code easy to read, maintain, and extend.
- **CLI-based Interaction**: All operations are handled via terminal prompts, making it lightweight and easy to use without a GUI.

## Key Techniques

- **Python-MySQL Integration**: Utilizes `mysql.connector` for seamless database operations.
- **Dynamic Table Creation**: Ensures tables and database are present before transactions.
- **SQL Parameterization**: Prevents SQL injection and ensures safe data handling.
- **Menu-Driven Interface**: Clear command-line menu for user-friendly operation.
- **Role-Dependent Menus**: Menu adapts to the logged-in user's role, showing only allowed actions.

## Database Schema

Three tables are automatically created:
- **pystudent**: `id`, `name`, `_class`, `roll_number` (unique), `gender` (`M`/`F`)
- **pystaff**: `id`, `name`, `gender` (`M`/`F`), `subject`, `salary`
- **users**: `id`, `username` (unique), `password`, `role` (`admin`, `staff`, `student`)

> **Security Note:** The code uses plain-text passwords. For production use, consider implementing password hashing and secure authentication.

## Key Learnings

- **Database Schema Design**: Structuring tables for school data, including unique constraints and ENUM fields for gender and roles.
- **Role-Based Access Control**: Implementing logic so only authorized users can perform sensitive operations.
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

4. **Create Initial Users**  
   You must add users to the `users` table directly in MySQL before running the app (for initial login), for example:
   ```sql
   INSERT INTO pyschool.users (username, password, role) VALUES ('admin1', 'adminpass', 'admin');
   INSERT INTO pyschool.users (username, password, role) VALUES ('staff1', 'staffpass', 'staff');
   ```
   *Note: The CLI does not provide user registration—add users directly via SQL.*

5. **Run the Application**  
   ```bash
   python school_management_system.py
   ```

6. **Follow Menu Prompts**  
   Add, search, or delete student/staff records as required. Menus will adapt based on your user role.

## Example Usage

```bash
$ python school_management_system.py
 ******** SCHOOL MANAGEMENT SYSTEM ******** 
 Successfully connected to database 
 LOGIN
 Username: admin1
 Password: *****
 Login successful! Role: admin

--- MENU ---
1 = Add Student
2 = Add Staff
3 = Search Student
4 = Search Staff
5 = Delete Student
6 = Delete Staff
7 = Exit
```

> If you log in as a staff member, only permitted actions will be shown:
```
--- MENU ---
1 = Add Student
3 = Search Student
4 = Search Staff
7 = Exit
```

## Strengths

- **Ease of Use**: Simple and direct interaction for managing records.
- **Extensibility**: Modular code can be adapted for more features (attendance, grading, etc.).
- **Reliability**: Database-backed system ensures data is persistent and reliable.
- **Security**: Role-based access restricts unauthorized actions.

## License

MIT License

---

*Happy Learning & Building!*
