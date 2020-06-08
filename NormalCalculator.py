def start():
    #Operator picker
    operators = ["+", "-", "*", "/"]
    option = int(input("Which operator would you like to use:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
    if option == 1:
        operator = operators[0]
    if option == 2:
        operator = operators[1]
    if option == 3:
        operator = operators[2]
    if option == 4:
        operator = operators[3]

    #Number picker
    numbers = []
    a = 1
    print('Type "Finish" when done')
    while True:
        option = input("Number {}: ".format(a))
        try:
            float(option)
        except ValueError:
            if str(option.lower()) == "finish":
                break
            else:
                print("Error")
                a -= 1
        else:
            numbers.append(option)
        a += 1
    if operator == "+":
        addition(numbers)
    elif operator == "-":
        subtraction(numbers)
    elif operator == "*":
        multiplication(numbers)
    elif operator == "/":
        division(numbers)
    

def addition(numbers):
    print("Addition")
    awnser = 0
    a = 0
    b = len.numbers()
    while a < b - 1:
        awnser += numbers[a] + numbers[a + 1]

    
def subtraction(numbers):
    print("subtraction")
    a = 0
    b = numbers.len()

    
def multiplication(numbers):
    print("multiplication")
    a = 0
    b = numbers.len()

    
def division(numbers):
    print("division")
    a = 0
    b = numbers.len()

    

start()
