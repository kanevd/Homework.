def calculate():
    choice = input
    
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter a choice: ")

num1 = float (input ("Enter first number: "))
num2 = float (input ("Enter second number: "))

if choice == "1":
    print ("Result is: ", end = ' '); print (num1 + num2)
elif choice == "2":
    print ("Result is: ", end = ' '); print (num1 - num2)
elif choice == "3":
    print ("Result is: ", end = ' '); print (num1 * num2)
elif choice == "4":
    print ("Result is: ", end = ' '); print (num1 / num2)
else: print ("Invalid input")

def again():
    choice2 = input ("Would you like to do a new calculation? Enter yes or no: ")
    if choice2 == "yes": 
        calculate()
    elif choice2 == "no":
        print("Bye.")