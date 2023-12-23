def print_triangle(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(' ', end='')
        for k in range(0, i + 1):
            print('* ', end='')
        print()

# Get the input from the user
num_rows = int(input('Enter the number of rows: '))

# Call the function with user input
print_triangle(num_rows)
