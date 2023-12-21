#inputting 2 strings
str1 = input('enter 1st string----> ')
str2 = input('enter 2nd string----> ')

#looping for the execution
if (len(str1)==len(str2)):
    a=str1.lower()
    b=str2.lower()
    if (sorted(a) == sorted(b)):
        print('the string is anagram')
else:
    print('the string is not anagram')
