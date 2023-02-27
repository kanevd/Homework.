#define functions for the different operations
def Add(num1,num2):
    return num1 + num2
 
def Substract(num1,num2):
    return num1 - num2
 
def Multiply(num1,num2):
    return num1 * num2
 
def Divide(num1,num2):
    return num1 / num2

#function for a new calculation
def repeat():
    choice2 = input("Would you like to do a new calculation? Enter yes or no: ")
    if choice2 == "yes":
        calculate()
    elif choice2 == "no":
        print("Bye.")
        return
    else:
        print("Invalid input")
        repeat()
 
#calculate menu
def calculate():
    operation = input('''
Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
Enter a choice:
''')
 
#proceeding with the calculation if one of the correct operation is selected
    if operation == "1" or operation == "2" or operation == "3" or operation == "4":
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == "4" and (num1 <= 0 or num2 <= 0): #division by zero check
                    print("Division by zero error handling");
                    repeat()
                    return
                elif operation == "4" and (num1 > 0 and num2 > 0):
                    print(f"Result is: {num1} / {num2} = {Divide(num1,num2)}")
                elif operation == "1":
                    print(f"Result is: {num1} + {num2} = {Add(num1,num2)}")
                elif operation == "2":
                    print(f"Result is: {num1} - {num2} = {Substract(num1,num2)}")
                elif operation == "3":
                    print(f"Result is: {num1} * {num2} = {Multiply(num1,num2)}")
 
                else: #checking for invalid inputs below
                    print("Invalid input")
                    repeat()
                    return
                repeat()
                return
            except ValueError:
                print("Invalid input")
                repeat()
                break
    else:
        print("Invalid input")
        repeat()
 
calculate()
