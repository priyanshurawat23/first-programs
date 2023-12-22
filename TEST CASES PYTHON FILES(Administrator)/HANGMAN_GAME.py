import random

def hangman_game(guesses):
    name = input('Enter your name ----> ')
    print('Hello', name, '\nWelcome to the Hangman game.')

    words = ['frown', 'rainbow', 'water', 'board', 'player', 'geeks', 'python', 'science', 'rough', 'miner']
    word = random.choice(words)
    print('You have to guess the characters, and you have 5 chances to guess. Good Luck!')

    guess = ''
    turns = 5

    while turns > 0:
        current_display = ''
        for ch in word:
            if ch in guess:
                current_display += ch
            else:
                current_display += '_'
        print(current_display)

        fail = sum(1 for ch in word if ch not in guess)

        if fail == 0:
            return 'win', word

        guesses = guesses.pop(0)
        guess += guesses

        if guesses not in word:
            turns -= 1
            print('Wrong, sorry.')
            print('You have', turns, 'guesses left.')

            if turns == 0:
                return 'lose', word

    return 'lose', word  # If the loop ends without a win, return 'lose' as a default