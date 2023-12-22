def is_palindrome(phrase):
    cleaned_phrase = phrase.replace(",", "").replace(";", "").replace(":", "").replace("!", "").replace("?", "").replace(".", "").replace("-", "").replace("'", "").replace(" ", "").lower()
    
    if cleaned_phrase == cleaned_phrase[::-1]:
        return True
    else:
        return False

def main():
    phrase = input('Enter a string ---> ')
    
    if is_palindrome(phrase):
        print('String is palindrome.')
    else:
        print('String is not palindrome.')

if __name__ == "__main__":
    main()
