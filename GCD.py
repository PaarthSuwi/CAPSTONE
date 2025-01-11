def find_gcd():
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    result = gcd(num1, num2)
    print("GCD of", num1, "and", num2, "is:", result)

find_gcd()

def find_factors():
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    def find_factors_of_num(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    factors_of_num1 = find_factors_of_num(num1)
    factors_of_num2 = find_factors_of_num(num2)

    print("Factors of", num1, "are:", factors_of_num1)
    print("Factors of", num2, "are:", factors_of_num2)

find_factors()