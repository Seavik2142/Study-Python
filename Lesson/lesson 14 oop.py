# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance < 0:
#             raise ValueError("Balance cannot be negative.")
#         self.__balance = new_balance

# account = BankAccount(1000)
# account.balance = -500 # This will raise a ValueError
# account.balance = 1500 # This will update the balance to 1500

# print(account.balance)

# class User:
#     def __init__(self, username):
#         self.__username = username


#     @property
#     def username(self):
#         return self.__username

#     @username.deleter
#     def username(self):
#         del self.__username

# user = User("john_doe")
# print(user.username)  # Output: john_doe
# del user.username  # Deletes the username attribute

class Student:
    def __init__(self, name , age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string.")
        if len(new_name.strip()) <3:
            raise ValueError("Name must be at least 3 characters long.")

        self.__name = new_name.strip()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise ValueError("Age must be an integer.")
        if new_age < 16:
            raise ValueError("Age must be at least 16.")
        self.__age = new_age


student1 = Student("Seavik", 21)

print(student1.name)
print(student1.age)

student1.age = 22

print("Updated Age:", student1.age)