
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
user_input = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {user_input} is: {factorial(user_input)}")