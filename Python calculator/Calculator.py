def Add(num1,num2):
    return num1+num2
 
def Substract(num1,num2):
    return num1 - num2
 
def Multiply(num1,num2):
    return num1 * num2
 
def Divide(num1,num2):
    return num1 / num2
 
def calculate():
    operation = input('''
Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
Enter a choice:
''')
 
    if operation == "1" or operation == "2" or operation == "3" or operation == "4":
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == "4" and num1 <= 0 or num2 <= 0:
                    print("division by zero error handling");
                    repeat()
 
                if operation == "1":
                    print(f"Result is: {num1} + {num2} = {Add(num1,num2)}")
                elif operation == "2":
                    print(f"Result is: {num1} - {num2} = {Substract(num1,num2)}")
                elif operation == "3":
                    print(f"Result is: {num1} * {num2} = {Multiply(num1,num2)}")
                elif operation == "4":
                    print(f"Result is: {num1} / {num2} = {Divide(num1,num2)}")
                else:
                    print("Invalid input")
 
                repeat()
            except ValueError:
                print("Invalid input")
                repeat()
                break
 
    else:
        print("Invalid input")
        repeat()
 
def repeat():
    choice2 = input("Would you like to do a new calculation? Enter yes or no: ")
    if choice2 != "yes" or choice2 != "no":
        print("Invalid input")
        repeat()
 
    if choice2 == "yes":
        calculate()
    elif choice2 == "no":
        print("Bye.")
 
calculate()
