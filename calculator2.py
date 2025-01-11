def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

def squareroot(x):
    return x ** (1 / 2)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def calc():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Factorial")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            num = float(input("Enter a number: "))
            print(f"Result: {squareroot(num)}")
        elif choice == '6':
            num = int(input("Enter a number: "))
            print(f"Result: {factorial(num)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calc()