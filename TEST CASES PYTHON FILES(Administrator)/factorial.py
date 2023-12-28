def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Get user input for the number
user_input = int(input("Enter a number: "))

# Call the function and store the result
factorial_result = calculate_factorial(user_input)

# Display the result
print(f"Factorial of {user_input} is {factorial_result}")
