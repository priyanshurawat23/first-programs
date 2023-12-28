def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input for Fahrenheit temperature
user_input = float(input("Enter temperature in Fahrenheit: "))

# Call the function and store the result
celsius_result = fahrenheit_to_celsius(user_input)

# Display the result
print(f"{user_input} F is equal to {celsius_result} C.")
