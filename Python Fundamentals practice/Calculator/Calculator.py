import math
### Simple Function that gets a number that the user inputs
def Get_number():
    while True:
        try:
            number = float(input("enter a number: "))
            return number
### If the user does not input a number or a number with a decimal, then it will give an error
        except ValueError: 
            print("Invalid input. Please enter a valid number.")

### This function gets the calculation that the user want to do            
def Get_calculation():
    while True:
        calculation = input("enter a calculation (+, -, *, /, s, r, % ): ")
        if calculation in ['+', '-', '*', '/', 's', 'r', '%']:
            return calculation
        else: ### error message will occur if the user inputs an invalid calculation
            print("Invalid input. Please enter a valid calculation.")
 
    ### This function does the calculation that the user wants to do           
def calculator():
    Num1 = Get_number()
    Calc = Get_calculation()
    Num2 = Get_number()
    if Calc == "+":
         result = Num1 + Num2   
    elif Calc == "-":
            result = Num1 - Num2
    elif Calc == "*":
            result = Num1 * Num2
    elif Calc == "/":
        if Num2 != 0: ### A number can't be divided by zero, so an error message will be displayed
                result = Num1 / Num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif Calc == "%":
        if Num2 != 0: ### A number can't be divided by zero, so an error message will be displayed
                result = Num1 % Num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif Calc == "s":
        result = math.pow(Num1, Num2)
    elif Calc == "r":
        result = math.pow(Num1, 1/Num2)
    print("The result is: ", result)
 ### The loop allows the user to do more than one calculation without needing to restart the program   
while True:
    calculator()
    again = input("Do you want to perform another calculation? (y/n): ")
    if again.lower() != "y":
        print("Goodbye!")
        break
    

    
