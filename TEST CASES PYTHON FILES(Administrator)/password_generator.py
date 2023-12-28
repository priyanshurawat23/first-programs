import random

def generate_strong_password(length):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_characters = '!@#$%^&*()-=_+[]{}|;:,.<>?'

    # Ensure the password length is at least 4
    if length < 4:
        raise ValueError("Password length must be at least 4")

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    random.shuffle(password)

    return ''.join(password)

# Get user input for password length
user_length = int(input("Enter the desired password length: "))

# Call the function and store the result
generated_password = generate_strong_password(user_length)

# Display the result
print("Generated Strong Password:", generated_password)
