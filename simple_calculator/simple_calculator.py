# Simple Calculator with Variable-Length Arguments

# Function to add multiple numbers
def addition(*args):
    return sum(args)

# Function to subtract multiple numbers
def substraction(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

# Function to multiply multiple numbers
def multiplication(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Function to divide multiple numbers
def division(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

# Prompt user to enter numbers separated by spaces
print("Enter numbers separated by spaces:")
numbers = list(map(int, input().split()))

# Display operation choices
print("Please select the operation you want to perform")
print("1.. for Addition")
print("2.. for Substraction")
print("3.. for Multiplication")
print("4.. for Division")

# Get the user's choice of operation
choice = int(input("Select the operation you want (1/2/3/4) "))

# Perform the selected operation
if choice == 1:
    print("The addition for the numbers: ", addition(*numbers))
elif choice == 2:
    print("The substraction for the numbers: ", substraction(*numbers))
elif choice == 3:
    print("The multiplication for the numbers: ", multiplication(*numbers))
elif choice == 4:
    print("The division for the numbers: ", division(*numbers))
else:
    print("Invalid choice, please try again.")