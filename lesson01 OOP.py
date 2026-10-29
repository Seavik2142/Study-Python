# class Student:
#     pass

# student1 = Student()
# student2 = Student()


# student1.name = "Alice"
# student2.name = "Bob"

# print(student1.name)
# print(student2.name)


# class Student:
#     pass

# student1 = Student()
# student1.name = "Vicheka"

# print(student1.name)


# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

# student1 = Student("Vicheka", 20)


# print(student1.name)
# print(student1.age)

# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# student1 = Student("Vicheka", 20)
# student1.show_info()



# class Student:
#     def __init__(self , name , math , english):
#         self.name = name
#         self.math = math
#         self.english = english

#     def calculate_average(self):
#         return (self.math + self.english) / 2

#     def show_info(self):
#         average_score = self.calculate_average()


#         print(f"Name students: {self.name}")
#         print(f"Average score: {average_score}")


# student1 = Student("Vicheka", 90, 85)
# student1.show_info()
        

# class Song:
#     def __init__(self, title , artist , price):
#         self.title = title
#         self.artist = artist
#         self.price = price


#     def show_info(self):
#         print(f"Title: {self.title}")
#         print(f"Artist: {self.artist}")
#         print(f"Price: ${self.price}")


#     def apply_discount(self, discount_percentage):
#         self.price -= self.price * (1 - discount_percentage / 100)


# song1 = Song("Khmer Song A", "Artist A", 2.99)
# song1.show_info()

# song1.apply_discount(10)  # Apply a 10% discount
# print("\nAfter applying discount:")
# song1.show_info()

# class Student:
#     def __init__(self , name , math , english):
#         self.name = name
#         self.math = math
#         self.english = english

#     def calculate_average(self):
#         return (self.math + self.english) / 2

#     def show_info(self):
#         average_score = self.calculate_average()
#         print(f"Name students: {self.name}")
#         print(f"Average score: {average_score}")

# student1 = Student("Vicheka", 70, 90)
# student1.show_info()

# class Student:
#     def __init__(self , name , age , score):
#         self.name = name
#         self.age = age
#         self.score = score

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Score: {self.score}")
#         print("-" * 20)

# students = [
#     Student("Vicheka", 20, 85),
#     Student("Sophea", 19, 90),
#     Student("Rithy", 21, 78)
# ]

# for student in students:
#     student.show_info()

# class Student:
#     def __init__(self , name , score ):
#         self.name = name
#         self.score = score

#     def check_result(self):
#         if self.score >= 50:
#             print(f"{self.name} has passed with a score of {self.score}.")
#         else:
#             print(f"{self.name} has failed with a score of {self.score}.")



# Students = [
#     Student("Vicheka", 80),
#     Student("Sophea", 40),
# ]

# for student in Students:
#     student.check_result()


# class Student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score

#     def check_result(self):
#         if self.score >= 50:
#             result = "passed"
#         else:
#             result = "failed"

#         print(f"{self.name}: {self.score} - {result}")


# students = [
#     Student("Vicheka", 80),
#     Student("Sophea", 40),
#     Student("Rithy", 90),
#     Student("Sokha", 45),
# ]

# for student in students:
#     student.check_result()

# class Student:
#     def __init__(self , name , score):
#         self.name = name
#         self.score = score

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Score: {self.score}")

# student1 = Student("Vicheka", 80)


# while True:
#     print("\nMenu:")
#     print("1. Show student info")
#     print("2. Update score")
#     print("3. Exit")

#     choice = input("Choose an option : ")

#     if choice == "1":
#         student1.show_info()
#     elif choice == "2":
#         print("Good bye!")
#         break

#     else:
#         print("Invalid choice. Please try again.")


# class Student:
#     def __init__(self , name , age , ID , score):
#         self.name = name
#         self.age = age
#         self.ID = ID
#         self.score = score

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"ID: {self.ID}")
#         print(f"Score: {self.score}")

# students = [
#     Student("Vicheka", 20, "S001", 85),
#     Student("Sophea", 19, "S002", 90),
#     Student("Rithy", 21, "S003", 78)
# ]

# while True:
#     print("\nMenu:")
#     print("1. Show all students info")
#     print("2. Search for a student by ID")
#     print("3. Exit")

#     choice = input("Choose an option 1-3: ")

#     if choice == "1":
#         for student in students:
#             student.show_info()
#             print("-" * 20)
#     elif choice == "2":
#         search_id = input("Enter the student ID to search: ")
#         found = False
#         for student in students:
#             if student.ID == search_id:
#                 student.show_info()
#                 found = True
#                 break
#         if not found:
#             print(f"Student with ID {search_id} not found.")
#     elif choice == "3":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# class BankAccount:
#     def __init__(self , balance):
#         self.balance = balance


# account = BankAccount(100)

# print(account.balance)  # Output: 100

# account.balance = -500

# print(account.balance)  # Output: -500 (This should not be allowed)





# class BankAccount:
#     def __init__(self , balance):
#         if balance >= 0:
#             self.__balance = balance
#         else:
#             self.__balance = 0

#     def deposit(self , amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}. New balance: ${self.__balance}.")
#         else:
#             print("Deposit amount must be positive > 0.")

#     def withdraw(self , amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive > 0.")

#         elif amount > self.__balance:
#             print("Insufficient funds for withdrawal.")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew: ${amount}. New balance: ${self.__balance}.")

#     def Show_balance(self):
#         print(f"Current balance: ${self.__balance}.")


# account = BankAccount(100)

# account.Show_balance()  # Output: Current balance: $100.
# account.deposit(50)     # Output: Deposited: $50. New balance: $150.
# account.withdraw(30)    # Output: Withdrew: $30. New balance:
# account.Show_balance()



# class Student:
#     def __init__(self , score):
#         self.__score = score

#     @property
#     def score(self):
#         return self.__score


# student1 = Student(85) 
# print(student1.score)  # Output: 85


# class Student:
#     def __init__(self , score):
#         self.score = score

#     @property
#     def score(self):
#         return self.__score

#     @score.setter
#     def score(self , value):
#         if 0 <= value <= 100:
#             self.__score = value
#         else:
#             print("Score must be between 0 and 100.")

# student1 = Student(85)
# print(student1.score)  # Output: 85

# student1.score = 95
# print(student1.score)  # Output: 95

# student1.score = 150  # Invalid score


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}. New balance: ${self.__balance}.")
#         else:
#             print("Deposit must be greater than 0.")
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal must be greater than 0.")
#         elif amount > self.__balance:
#             print("Insufficient funds for withdrawal.")
#         else:
#             self.__balance -= amount
#             print(f"Withdrew: ${amount}. New balance: ${self.__balance}.")
        
#     def show_balance(self):
#         print(f"Current balance: ${self.__balance}.")
        


# account = BankAccount(100)
# account.deposit(-30)
# account.withdraw(130)    
# account.show_balance()

# class Animal:
#     def eat(self):
#         print("Animal is eating.")

#     def sleep(self):
#         print("Animal is sleeping.")

# class Dog(Animal):
#     def bark(self):
#         print("Wolf Wolf!")


# dog = Dog()
# dog.eat()   # Inherited from Animal class
# dog.sleep() # Inherited from Animal class
# dog.bark()  # Specific to Dog class


# class Person:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# class Student(Person):
#     def __init__(self , name , age , student_id):
#         super().__init__(name , age)
#         self.student_id = student_id

#     def show_student_id(self):
#         print(f"Student ID: {self.student_id}")


# student1 = Student("Vicheka", 20, "S001")
# student1.show_info()  
# student1.show_student_id()

# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound.")

# class Dog(Animal):
#     def make_sound(self):
#         print("Wolf Wolf!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow Meow!")


# dog = Dog()
# cat = Cat()

# dog.make_sound()  # Output: Wolf Wolf!
# cat.make_sound()  # Output: Meow Meow!


# class user:
#     def __init__(self , username , password):
#         self.username = username
#         self.__password = password

#     def show_info(self):
#         print(f"Username: {self.username}")
#         print(f"Password: [HIDDEN]")  # Do not display the actual password
# class Admin(user):
#     def __init__(self , username , password , admin_level):
#         super().__init__(username , password)
#         self.admin_level = admin_level

#     def show_admin_info(self):
#         self.show_info()
#         print(f"Admin Level: {self.admin_level}")

# class Staff(user):
#     def __init__(self , username , password , staff_id):
#         super().__init__(username , password)
#         self.staff_id = staff_id

#     def show_staff_info(self):
#         self.show_info()
#         print(f"Staff ID: {self.staff_id}")

# class Student(user):
#     def __init__(self , username , password , student_id):
#         super().__init__(username , password)
#         self.student_id = student_id

#     def show_student_info(self):
#         self.show_info()
#         print(f"Student ID: {self.student_id}")

# admin = Admin("admin_user", "admin_pass", 1)
# admin.show_admin_info()

# print("-" * 30)

# staff = Staff("staff_user", "staff_pass", "S001")
# staff.show_staff_info()

# print("-" * 30)

# student = Student("student_user", "student_pass", "ST001")
# student.show_student_info()


# from tkinter import HIDDEN


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = [HIDDEN]  # Private attribute

#     def show_info(self):
#         print(f"Username: {self.username}")
#         print(f"Password: [HIDDEN]")  # Do not display the actual password

#     def check_password(self, password):
#         return self.__password == password

# class Admin(User):
#     def __init__(self, username, password, admin_level):
#         super().__init__(username, password)
#         self.admin_level = admin_level

#     def show_admin_info(self):
#         self.show_info()
#         print(f"Admin Level: {self.admin_level}")

#     def get_role(self):
#         return "Admin"

# class Staff(User):
#     def __init__(self, username, password, staff_id):
#         super().__init__(username, password)
#         self.staff_id = staff_id

#     def show_staff_info(self):
#         self.show_info()
#         print(f"Staff ID: {self.staff_id}")

#     def get_role(self):
#         return "Staff"

# class Student(User):
#     def __init__(self, username, password, student_id):
#         super().__init__(username, password)
#         self.student_id = student_id

#     def show_student_info(self):
#         self.show_info()
#         print(f"Student ID: {self.student_id}")

#     def get_role(self):
#         return "Student"

# admin = Admin("admin_user", "admin_pass123", 1)
# admin.show_admin_info()

# print("-" * 30)

# staff = Staff("staff_user", "staff_pass123", "S001")
# staff.show_staff_info()

# print("-" * 30)

# student = Student("student_user", "student_pass123", "ST001")
# student.show_student_info()





# import hashlib
# import secrets
# import hmac


# class User:
#     def __init__(self, username, password):
#         if not isinstance(username, str) or not username.strip():
#             raise ValueError("Username cannot be empty.")

#         if not isinstance(password, str) or len(password) < 8:
#             raise ValueError("Password must contain at least 8 characters.")

#         self.username = username
#         self.__salt = secrets.token_bytes(16)
#         self.__password_hash = self.__hash_password(password)

#     def __hash_password(self, password):
#         return hashlib.scrypt(
#             password.encode("utf-8"),
#             salt=self.__salt,
#             n=2**14,
#             r=8,
#             p=1
#         )

#     def check_password(self, password):
#         if not isinstance(password, str):
#             return False

#         candidate_hash = self.__hash_password(password)

#         return hmac.compare_digest(
#             self.__password_hash,
#             candidate_hash
#         )

#     def show_info(self):
#         print(f"Username: {self.username}")
#         print("Password: [HIDDEN]")

#     def get_role(self):
#         return "User"


# class Admin(User):
#     def __init__(self, username, password, admin_level):
#         super().__init__(username, password)

#         if not isinstance(admin_level, int) or admin_level < 1:
#             raise ValueError("Admin level must be a positive integer.")

#         self.admin_level = admin_level

#     def get_role(self):
#         return "Admin"

#     def show_admin_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Admin Level: {self.admin_level}")


# class Staff(User):
#     def __init__(self, username, password, staff_id):
#         super().__init__(username, password)

#         if not isinstance(staff_id, str) or not staff_id.strip():
#             raise ValueError("Staff ID cannot be empty.")

#         self.staff_id = staff_id

#     def get_role(self):
#         return "Staff"

#     def show_staff_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Staff ID: {self.staff_id}")


# class Student(User):
#     def __init__(self, username, password, student_id):
#         super().__init__(username, password)

#         if not isinstance(student_id, str) or not student_id.strip():
#             raise ValueError("Student ID cannot be empty.")

#         self.student_id = student_id

#     def get_role(self):
#         return "Student"

#     def show_student_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Student ID: {self.student_id}")


# admin = Admin("admin_user", "admin_pass123", 1)
# admin.show_admin_info()

# print("Password valid:", admin.check_password("admin_pass123"))
# print("Password valid:", admin.check_password("wrong_password"))


# import hashlib
# import secrets
# import hmac


# class User:
#     def __init__(self, username, password):
#         if not isinstance(username, str) or not username.strip():
#             raise ValueError("Username cannot be empty.")

#         if not isinstance(password, str) or len(password) < 8:
#             raise ValueError("Password must contain at least 8 characters.")

#         self.username = username
#         self.__salt = secrets.token_bytes(16)
#         self.__password_hash = self.__hash_password(password)

#     def __hash_password(self, password):
#         return hashlib.scrypt(
#             password.encode("utf-8"),
#             salt=self.__salt,
#             n=2**14,
#             r=8,
#             p=1
#         )

#     def check_password(self, password):
#         if not isinstance(password, str):
#             return False

#         candidate_hash = self.__hash_password(password)

#         return hmac.compare_digest(
#             self.__password_hash,
#             candidate_hash
#         )

#     def show_info(self):
#         print(f"Username: {self.username}")
#         print("Password: [HIDDEN]")

#     def get_role(self):
#         return "User"


# class Admin(User):
#     def __init__(self, username, password, admin_level):
#         super().__init__(username, password)

#         if type(admin_level) is not int or admin_level < 1:
#             raise ValueError("Admin level must be a positive integer.")

#         self.admin_level = admin_level

#     def get_role(self):
#         return "Admin"

#     def show_admin_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Admin Level: {self.admin_level}")


# class Staff(User):
#     def __init__(self, username, password, staff_id):
#         super().__init__(username, password)

#         if type(staff_id) is not str or not staff_id.strip():
#             raise ValueError("Staff ID cannot be empty.")

#         self.staff_id = staff_id

#     def get_role(self):
#         return "Staff"

#     def show_staff_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Staff ID: {self.staff_id}")

# class Student(User):
#     def __init__(self, username, password, student_id):
#         super().__init__(username, password)

#         if not isinstance(student_id, str) or not student_id.strip():
#             raise ValueError("Student ID cannot be empty.")

#         self.student_id = student_id

#     def get_role(self):
#         return "Student"

#     def show_student_info(self):
#         self.show_info()
#         print(f"Role: {self.get_role()}")
#         print(f"Student ID: {self.student_id}")

# while True:
#     print("\nMenu:")
#     print("1. Create Admin")
#     print("2. Create Staff")
#     print("3. Create Student")
#     print("4. Exit")

#     choice = input("Choose an option 1-4: ")

#     if choice == "1":
#         username = input("Enter admin username: ")
#         password = input("Enter admin password (min 8 characters): ")
#         admin_level = int(input("Enter admin level (positive integer): "))
#         try:
#             username = input("Enter admin username: ")
#             password = input("Enter admin password: ")
#             admin_level = int(input("Enter admin level: "))

#             admin = Admin(username, password, admin_level)
#             admin.show_admin_info()

#         except ValueError as e:
#             print(f"Error: {e}")
#     elif choice == "2":
#         username = input("Enter staff username: ")
#         password = input("Enter staff password (min 8 characters): ")
#         staff_id = input("Enter staff ID: ")
#         try:
#             staff = Staff(username, password, staff_id)
#             staff.show_staff_info()
#         except ValueError as e:
#             print(f"Error: {e}")

#     elif choice == "3":
#         username = input("Enter student username: ")
#         password = input("Enter student password (min 8 characters): ")
#         student_id = input("Enter student ID: ")
#         try:
#             student = Student(username, password, student_id)
#             student.show_student_info()
#         except ValueError as e:
#             print(f"Error: {e}")

#     elif choice == "4":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please try again.")




# class User:
#     def __init__(self, username, password):
#         if not isinstance(username, str) or not username.strip():
#             raise ValueError("Username cannot be empty.")
#         if not isinstance(password, str) or len(password) < 8:
#             raise ValueError("Password must contain at least 8 characters.")

#         self.username = username
#         self.__password = password

#     def show_info(self):
#         print(f"Username: {self.username}")
#         print("Password: [HIDDEN]")

#     def check_password(self, password):
#         return self.__password == password

#     def get_role(self):
#         return "User"
# class Admin(User):
#     def get_role(self):
#         return "Admin"

# class Staff(User):
#     def get_role(self):
#         return "Staff"

# class Student(User):
#     def get_role(self):
#         return "Student"

# users = [
#     Admin("admin", "adminpass123"),
#     Staff("staff", "staffpass123"),
#     Student("student", "studentpass123")
# ]

# for user in users:
#     print(user.get_role())

# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass


# class ABA(Payment):
#     def process_payment(self, amount):
#         print(f"Processing ABA payment of ${amount}.")

# class Acleda(Payment):
#     def process_payment(self, amount):
#         print(f"Processing Acleda payment of ${amount}.")

# payments = [
#     ABA(), 
#     Acleda()
# ]

# amount = [100, 200]

# for payment, amt in zip(payments, amount):
#     payment.process_payment(amt)

# class Engine:
#     def start(self):
#         print("Engine started.")

#     def stop(self):
#         print("Engine stopped.")

# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def start(self):
#         self.engine.start()
#         print("Car is ready to go!")

#     def stop(self):
#         self.engine.stop()
#         print("Car has stopped.")

# while True:
#     print("\nMenu:")
#     print("1. Start the car")
#     print("2. Stop the car")
#     print("3. Exit")

#     choice = input("Choose an option 1-3: ")

#     if choice == "1":
#         car = Car()
#         car.start()
#     elif choice == "2":
#         car.stop()
#     elif choice == "3":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")



# class CPU:
#     def __init__(self, model):
#         self.model = model

#     def process(self):
#         print(f"{self.model} CPU is processing data.")

# class Computer:
#     def __init__(self, cpu_model):
#         self.cpu = CPU(cpu_model)

#     def start(self):
#         self.cpu.process()
#         print("Computer is starting.")

# while True:
#     print("\nMenu:")
#     print("1. Start the computer")
#     print("2. Exit")

#     choice = input("Choose an option 1-2: ")

#     if choice == "1":
#         cpu_model = input("Enter CPU model: ")
#         computer = Computer(cpu_model)
#         computer.start()
#     elif choice == "2":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")



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

    choice = input("Please choose an option (1-5): ").strip()

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
                choice = input("Please choose an option (1 & 2): ").strip()
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
                            print("Teacher not found.")

                elif choice == "2":
                    student_id = input("Enter Student ID to Search ")
                    found = False

                    for student in student:
                        if student.student_id ==student_id:
                            print("nStudent Found!")
                            student.show_student_info()
                            found = True
                            break
                        if not found:
                            print("Student not found")
                    
                else:
                    print("Invalid choice. Please choose 1-5.")
                    


        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")

    except ValueError as error:
        print(f"Error: {error}")
