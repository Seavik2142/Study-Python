# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))

# current_year = 2026
# age = current_year - birth_year

# print(f"Hello, {name}! You are {age} years old.")

# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(f"The sum of numbers from 1 to {n} is: {total}")

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter a number to check if it's even or odd: "))
# result = check_even_odd(num)
# print(f"The number {num} is {result}.")

# numbers = [12 , 45 , 2 , 89 , 34 , 67 , 10]

# max_number = max(numbers)
# min_number = min(numbers)

# avg_num = sum(numbers) / len(numbers)

# print(f"list of numbers: {numbers}")
# print(f"The maximum number is: {max_number}")
# print(f"The minimum number is: {min_number}")
# print(f"The average of the numbers is: {avg_num:.2f}")

# students = {
#     "Seavik": 85,
#     "Aarav": 92,
#     "Riya": 78, 
#     "Ananya": 88,
# }

# search_name = input("Enter the name of the student to search for their score: ")

# score = students.get(search_name)
# if score is not None:
#     print(f"{search_name}'s score is: {score}")
# else:
#     print(f"{search_name} is not found in the records.")

# def sefe_divide(a, b):
#     try:
#         result = a / b
#         return f"The result of {a} divided by {b} is: {result}"
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     except TypeError:
#         return "Error: Please provide valid numbers for division."


# print(sefe_divide(10, 2))  # Valid division
# print(sefe_divide(10, 0))  # Division by zero
# print(sefe_divide(10, "two"))  # Invalid type

# inventory = [
#     {"name": "Laptop", "price": 1000, "quantity": 5},
#     {"name": "Mouse", "price": 25, "quantity": 10},
#     {"name": "Keyboard", "price": 75, "quantity": 7}
# ]

# try:
#     item_name = input("input the name of item: ")
#     quantity = int(input("input the quantity of item: "))

#     found = False
#     for item in inventory:
#         if item["name"].lower() == item_name.lower():
#             found = True
#             if quantity <= item["quantity"]:
#                 total_price = item["price"] * quantity
#                 print(f"The total price for {quantity} {item_name}(s) is: ${total_price}")
#             else:
#                 print(f"Error: Only {item['quantity']} {item_name}(s) are available in stock.")
#             break
#     if not found:
#         print(f"Error: {item_name} is not found in the inventory.")
# except ValueError:
#     print("Error: Please enter a valid number for quantity.")


class Song:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show_info(self):
        print(f"Song: {self.title}")
        print(f"Price: ${self.price}")


# បង្កើត Objects ពី Class Song
song1 = Song("Khmer Song A", 2.99)
song2 = Song("Khmer Song B", 1.99)

song1.show_info()
song2.show_info()
