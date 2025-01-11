def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    num = input("Enter a number: ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

if __name__ == "__main__":
    main()


num = 121
if str (num) == str(num)[::-1]:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")