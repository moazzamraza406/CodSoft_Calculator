import os
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

operation_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calcultor():
    numb1 = float(input("Enter fisrt number: "))
    for symbol in operation_dict:
        print(symbol)
    continue_process=True
    while continue_process:
        op_symbol  = input("Pick an operation: ")
        numb2 = float(input("Enter next number: "))
        calculator_function = operation_dict[op_symbol]
        output = calculator_function(numb1,numb2)
        print(f"{numb1} {op_symbol} {numb2} = {output}")
        continue_cal = input("Enter 'y' for continue calculation with {output} or 'n' to start new calculation or 'x' to exit the calculation")
        if continue_cal == 'y':
            numb1 = output
        elif continue_cal== 'n':
            continue_process = False
            os.system('cls')
            calcultor()

        elif continue_cal == 'x' :
            continue_process = False
            print("Calculation is finished")
calcultor()