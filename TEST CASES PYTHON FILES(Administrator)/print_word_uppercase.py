def print_word_uppercase(word):
    x = ""
    for i in word:
        x += i
        print(x.upper())

# Get input from the user for the word
word = input('Enter the word you want to print: ')

# Call the function to print the word in uppercase
print_word_uppercase(word)
