class Calculator:
    """A Calculator class encapsulating basic arithmetic operations."""
    
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


def main():
    # Instantiate the Calculator object
    calc = Calculator()
    
    # Main application loop
    while True:
        print("\n==============================")
        print("       OOP CALCULATOR         ")
        print("==============================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Select an operation (1-5): ").strip()
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("⚠️ Invalid input! Please enter valid numeric values.")
                continue
                
            if choice == '1':
                result = calc.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("⚠️ Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()