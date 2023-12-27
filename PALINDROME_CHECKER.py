###WAP TO CHECK WHETHER A PHRASE IS PALINDROME OR NOT.###

#inputting a string from user
str1=input('enter a string---> ')


d = str1.replace(",", "").replace(";", "").replace(":", "").replace("!", "").replace("?", "").replace(".", "").replace("-", "").replace("'", "").replace(" ", "").lower()

#if-else loop for execution of purpose
if d==d[::-1]:
    print('string is palindrome')
else:
    print('string is not palindrome')

