import random
name=input('enter your name----> ')
print('hello',name, '\nwelcome to hangman game.')
words=['frown', 'rainbow', 'water', 'board', 'player', 'geeks', 'python', 'science', 'rough', 'miner']

word = random.choice(words)
print('you have to guess the character, and you have 5 chances to guess. Good Luck!')
guess=''
turn=5
while turn>0:
    fail=0
    for ch in word:
        if ch in guess:
            print(ch, end='')
        else:
            print('_', end=' ')
            fail+=1
    if fail==0:
        print('\nyou win')
        print('the correct word is', word)
        break
    print()
    guesses=input('guess a character--> ')
    guess+=guesses
    if guesses not in word:
        turn-=1
        print('wrong,sorry')
        print('you have' ,turn, 'guesses left')
        if turn==0:
            print('you lose')
