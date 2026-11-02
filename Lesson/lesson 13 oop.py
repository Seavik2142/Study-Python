# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Student Name: {self.name}, Age: {self.age}"

# student1 = Student("John", 20)
# print(student1)


# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Student (Name={self.name}, Age: {self.age})"

# student1 = Student("John", 20)
# print(student1)

# class Course:
#     def __init__(self, course_name, students):
#         self.course_name = course_name
#         self.students = students

#     def __len__(self):
#         return len(self.students)


# python_course = Course(
#     "Python OOP" , 
#     ["John", "Alice", "Bob"]
# )

# print(len(python_course))  # Output: 3


# class Student:
#     def __init__(self , student_id):
#         self.student_id = student_id

#     def __eq__(self , other):
#         if not isinstance(other, Student):
#             return NotImplemented
#         return self.student_id == other.student_id


# student1 = Student("S001")
# student2 = Student("S001")
# student3 = Student("S002")

# print(student1 == student2)  
# print(student1 == student3)

# class bankAccount:
#     def __init__(self , balance):
#         self.balance = balance

#     def __add__(self , other):
#         return self.balance + other.balance

# account1 = bankAccount(1000)
# account2 = bankAccount(2000)

# total_balance = account1 + account2
# print(total_balance)  # Output: 3000