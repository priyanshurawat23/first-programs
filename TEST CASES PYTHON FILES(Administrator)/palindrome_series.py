def is_palindrome(num):
    original_num = num
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original_num == reverse

def generate_palindromes(count):
    palindromes = []
    for i in range(1, count + 1):
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes

# Get user input for the number of palindromes to generate
n = int(input('How many palindrome numbers to generate: '))

# Generate and print palindromes
result = generate_palindromes(n)
print("Palindrome numbers:", result)
