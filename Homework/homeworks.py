import hashlib
import secrets
import hmac


# Parent Class
class User:
    def __init__(self, username, password):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username cannot be empty.")

        if not isinstance(password, str) or len(password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters."
            )

        self.username = username.strip()
        self.__salt = secrets.token_bytes(16)
        self.__password_hash = self.__hash_password(password)

    def __hash_password(self, password):
        return hashlib.scrypt(
            password.encode("utf-8"),
            salt=self.__salt,
            n=2**14,
            r=8,
            p=1
        )

    def check_password(self, password):
        if not isinstance(password, str):
            return False

        candidate_hash = self.__hash_password(password)

        return hmac.compare_digest(
            self.__password_hash,
            candidate_hash
        )

    def show_info(self):
        print(f"Username: {self.username}")
        print("Password: [HIDDEN]")

    def get_role(self):
        return "User"


# Admin Class
class Admin(User):
    def __init__(self, username, password, admin_level):
        super().__init__(username, password)

        if type(admin_level) is not int or admin_level < 1:
            raise ValueError(
                "Admin level must be a positive integer."
            )

        self.admin_level = admin_level

    def get_role(self):
        return "Admin"


# Teacher Class
class Teacher(User):
    def __init__(self, username, password, teacher_id):
        super().__init__(username, password)

        if not isinstance(teacher_id, str) or not teacher_id.strip():
            raise ValueError("Teacher ID cannot be empty.")

        self.teacher_id = teacher_id.strip()

    def get_role(self):
        return "Teacher"

    def show_teacher_info(self):
        self.show_info()
        print(f"Role: {self.get_role()}")
        print(f"Teacher ID: {self.teacher_id}")


# Student Class
class Student(User):
    def __init__(self, username, password, student_id):
        super().__init__(username, password)

        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        self.student_id = student_id.strip()

    def get_role(self):
        return "Student"

    def show_student_info(self):
        self.show_info()
        print(f"Role: {self.get_role()}")
        print(f"Student ID: {self.student_id}")


# Lists to store objects while the program is running
teachers = []
student_list = []


# Main Menu
while True:
    print("\n===== Norton University =====")
    print("1. Add Teacher")
    print("2. Add Student")
    print("3. Show All Teachers")
    print("4. Show All Students")
    print("5. Search Teachers And Students By ID.")
    print("6. Exit")

    choice = input("Please choose an option (1-6): ").strip()

    try:
        if choice == "1":
            username = input("Enter teacher username: ")
            password = input("Enter password (min 8 characters): ")
            teacher_id = input("Enter teacher ID: ")

            teacher = Teacher(username, password, teacher_id)
            teachers.append(teacher)

            print("Teacher added successfully!")

        elif choice == "2":
            username = input("Enter student username: ")
            password = input("Enter password (min 8 characters): ")
            student_id = input("Enter student ID: ")

            student = Student(username, password, student_id)
            student_list.append(student)

            print("Student added successfully!")

        elif choice == "3":
            print("\n===== Teacher List =====")

            if not teachers:
                print("No teachers found.")
            else:
                for teacher in teachers:
                    teacher.show_teacher_info()
                    print("-" * 30)

        elif choice == "4":
            print("\n===== Student List =====")

            if not student_list:
                print("No students found.")
            else:
                for student in student_list:
                    student.show_student_info()
                    print("-" * 30)
        elif choice == "5":
            while True:
                print("1. Teacher ID")
                print("2. Student ID")
                choice = input("Please choose an option (1 & 2 & 3): ").strip()
                if choice == "1":
                    teacher_id = input("Enter Teacher ID to Search:  ")
                    found = False

                    for teacher in teachers:
                        if teacher.teacher_id == teacher_id:
                            print("Teacher Found!")
                            teacher.show_teacher_info()
                            found = True
                            break
                        if not found:
                            print("\nTeacher not found.")

                elif choice == "2":
                    student_id = input("Enter Student ID to Search ")
                    found = False

                    for student in student_list:
                        if student.student_id ==student_id:
                            print("\nStudent Found!")
                            student.show_student_info()
                            found = True
                            break
                    if not found:
                        print("Student not found")
                    
                elif choice == "3":
                    print("Returing to Main Menu...")
                    break

                else:
                    print("Invalid choise. Please choose 1-3.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")

    except ValueError as error:
        print(f"Error: {error}")
