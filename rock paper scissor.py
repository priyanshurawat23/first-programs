import random
print('welcome to rock paper scissor game.\nrules of the game ROCK PAPER SCISSORS are :\nRock vs Paper --> Paper wins '
      + '\nRock vs Scissors --> Rock wins \nPaper vs Scissors --> Scissor wins \n')
while True:
    print('Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n')
    c=int(input('enter your choice---> '))
    if c== 1:
        ch= 'Rock'
    elif c== 2:
        ch= 'Paper'
    else:
        ch= 'Scissors'
    print('user choice is',ch)
    print('now its computers turn....')
    com = random.randint(1, 3)
    while com== ch:
        com= random.randint(1,3)
    if com== 1:
        comchoice= 'ROCK'
    elif com == 2:
        comchoice= 'PAPER'
    else:
        comchoice = 'SCISSOR'
    print("computer choice is \n", comchoice)
    print(ch, 'vs', comchoice)
    if c== com:
        print('its a Draw', end="")
        result = "DRAW"
    if (c== 1 and com== 2):
        print('paper wins =>', end="")
        result = 'paper'
    elif (c == 2 and com== 1):
        print('paper wins =>', end="")
        result = 'paper'
    if (c== 1 and com== 3):
        print('rock wins =>\n', end="")
        result = 'rock'
    elif (c== 3 and com== 1):
        print('rock wins =>\n', end="")
        result = 'rock'
    if (c== 2 and com== 3):
        print('scissors wins =>', end="")
        result = 'scissor'
    elif (c== 3 and com== 2):
        print('scissors wins =>', end="")
        result = 'rock'
    if result == 'DRAW':
        print("<== its a tie ==>")
    if result == ch:
        print("<== user wins ==>")
    else:
        print("<== computer wins ==>")
    print("do you want to play again? (Y/N)")
    ans = input().lower
    if ans == 'n':
        break
print("thanks for playing")
