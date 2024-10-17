def addition(a,b):
    y = a + b
    return y

    
def subtraction(a,b):
    y = a - b
    return y

def multiplication(a,b):
    y = a * b
    return y

def division(a,b):
    y = a/b
    return y

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
} 

def calculator():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the first number: '))
    operation = input("Enter an operation (+,-,*,/): ")
    
    if operation in operations:
        result = operations[operation](num1,num2)
        print(f"{num1},{operations},{num2} = {result}")
    else:
        print('Invalid operation')

calculator()