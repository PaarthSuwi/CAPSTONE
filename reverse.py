def reverse_number():
    num = int(input("Enter a number: "))
    reversed_num = 0
    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    print("Reversed Number:", reversed_num)
reverse_number()




def reverse_number():
    num = int(input("Enter a number: "))  
    reversed_num = 0
    reversed_digits = []
    while num != 0:
        digit = num % 10
        reversed_digits.append(str(digit))
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    print("Reversed Number with Spaces:", " ".join(reversed_digits))

reverse_number()




num = 12345
rev_num = 0
while num > 0:
    rev_num = rev_num*10 + num%10
    num //=10
print(" ".join(str(rev_num)))