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







