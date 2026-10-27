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


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}.")
        else:
            print("Deposit must be greater than 0.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}.")
        
    def show_balance(self):
        print(f"Current balance: ${self.__balance}.")
        


account = BankAccount(100)
account.deposit(-30)
account.withdraw(130)    
account.show_balance()