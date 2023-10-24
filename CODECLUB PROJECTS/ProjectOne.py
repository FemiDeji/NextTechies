# command line calculator
num = input("Enter an expression: ")
print(eval(num))


operator = input("Please enter an operator(+ - * /): ")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print("ERROR")

