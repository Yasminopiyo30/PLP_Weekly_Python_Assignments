#Intro to the python assignment
#Basic calculator app

#Step 1: Welcome message
print ("Welcome to the Basic calculator!")

#Step 2: Ask the user to enter the first number
#Float data type so they can enter whole numbers or decimals
num1 = float(input("Enter the first number: "))

#Step 3: Ask for the second number
num2 = float(input("Enter the second number: "))

#Step 4: Ask for the operation the user wants to input
operation = input("Enter the operation(+, -, *, /): ")

#Step 5: Show what they chose
print ("calculating...")

#Step 6: Doing the math based on the users choice
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif operation == "/":
    if num2 == 0:
        print("Error: You can't divide by zero!")
    else:
        result = num1 / num2
        print (num1, "/", num2, "=", result)

else:
    print("Sorry, I don't know that operation. Pleasee use +,-,*,or /")
