def get_user_input():
    str1 = input('Enter 1st string ----> ')
    str2 = input('Enter 2nd string ----> ')
    return str1, str2

def check_anagram(str1, str2):
    if len(str1) == len(str2):
        a = str1.lower()
        b = str2.lower()
        if sorted(a) == sorted(b):
            return True
    return False

def main():
    str1, str2 = get_user_input()

    if check_anagram(str1, str2):
        print('The strings are anagrams.')
    else:
        print('The strings are not anagrams.')

if __name__ == "__main__":
    main()