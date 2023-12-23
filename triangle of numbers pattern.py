rows = int(input('enter no. of rows--> '))
for i in range(1, rows+1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print(" ")
