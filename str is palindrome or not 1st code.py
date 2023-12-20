###1. to check if string is palindrome or not###

#inputting a string from user
str1=input('enter a string---> ')

#replacing any spaces with commas and converting all alphabets to lowercase
d= str1.replace(" ", "").lower()

#if-else loop for execution of purpose
if d==d[::-1]:
    print('string is palindrome')
else:
    print('string is not palindrome')

