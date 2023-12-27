import random

length = 16

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&*()-=_+[]{}|;:,.<>?'

password = [
    random.choice(lowercase_letters),
    random.choice(uppercase_letters),
    random.choice(digits),
    random.choice(special_characters)
]
all_characters = lowercase_letters + uppercase_letters + digits + special_characters
password.extend(random.choice(all_characters) for _ in range(length - 4))

random.shuffle(password)


password = ''.join(password)

print("Generated Strong Password:", password)
