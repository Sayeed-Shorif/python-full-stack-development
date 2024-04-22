# Python calculator
import sys

# take user input

def calculation(n, a, b):
    if n == '+':
        print(a + b)
    elif n == '-':
        print(a - b)
    elif n == '*':
        print(a * b)
    elif n == '/':
        try:
            print(a / b)
        except ZeroDivisionError:
            print("The number can't be devided by zero")
            sys.exit(1)
    else:
        print("Enter a valid symbol between + , - , * , / ")
        sys.exit(1)
        

try:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
except ValueError:
    print('Enter a valid number !')
    sys.exit(1)

calculation_symbol = input("Enter the calculation : available calculation (+, -, *, /) : ")

calculation(calculation_symbol, num1, num2)
