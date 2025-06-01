import time

name = input("Hello, this is my final project.\nWhat is your name? ")
print("Hi " + name + ", nice to meet you!")

print("\nThis is a simple calculator. Please enter 2 numbers.")

# input numbers
first_number = int(input("Before you press Enter, select the 1st number: "))
second_number = int(input("Before you press Enter, select the 2nd number: "))

# Even/odd test
is_even_second_number=second_number % 2 == 0

if first_number % 2 == 0:
    if (is_even_second_number):
        print("Both numbers are even.")
    else:
        print("The first number is even and the second is odd.")
else:
    if is_even_second_number:
        print("The first number is odd and the second is even.")
    else:
        print("Both numbers are odd.")

# choose operator
operator = input("Please choose an operator (+, -, *, /): ")

# Choose output format
number_type = input("Do you want the result shown as Integer? (y/n): ")

# Normalize and validate user input
answer = number_type.strip().lower()
yes_inputs = {"y", "yes"}
no_inputs = {"n", "no"}

if answer in yes_inputs:
    type_yes = number_type.strip().lower() == "y"#type_yes = True
elif answer in no_inputs:
    type_yes = False
else:
    print("Invalid input. Please enter one of the following: yes, no, y, or n (case and spacing do not matter).")
    exit()

# Operator validation
valid_operators = ["+", "-", "*", "/"]
if operator not in valid_operators:
    print("Error: The operator is invalid. Please enter +, -, *, or /.")
    exit()

# Convert to float if user chose decimal
if not type_yes:
    first_number = float(first_number)
    second_number = float(second_number)

# calculate result
if operator == "/" and second_number == 0:
    print("Error: The second number (the divisor) cannot be zero. Division by zero is undefined.")
else:
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        # Division has two forms: one returns an integer (//), the other returns a float (/).
        if type_yes: 
            result = first_number // second_number 
        else:
            result = first_number / second_number   

    # formatting result
    if type_yes:
        print(f"{first_number} {operator} {second_number} = {int(result)}")
    else:
        if isinstance(result, float):
            formatted = f"{result:.2f}"
            if formatted.endswith(".00"):
                formatted = str(int(float(formatted)))
            print(f"{first_number} {operator} {second_number} = {formatted}")
        else:
            print(f"{first_number} {operator} {second_number} = {result}")

# ending message
print("Thank you, " + name + ", for using the calculator on " + time.ctime() + ".")

