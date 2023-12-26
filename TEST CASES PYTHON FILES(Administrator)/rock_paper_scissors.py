import random

def play_game():
    print('Welcome to the Rock-Paper-Scissors game.')
    print('Rules of the game ROCK PAPER SCISSORS are:')
    print('Rock vs Paper --> Paper wins')
    print('Rock vs Scissors --> Rock wins')
    print('Paper vs Scissors --> Scissor wins\n')

    while True:
        print('Enter your choice:')
        print('1 - Rock')
        print('2 - Paper')
        print('3 - Scissors')

        user_choice = int(input('Enter your choice: '))
        if user_choice == 1:
            user_choice_str = 'Rock'
        elif user_choice == 2:
            user_choice_str = 'Paper'
        else:
            user_choice_str = 'Scissors'

        print('User choice is', user_choice_str)
        print('Now it\'s the computer\'s turn....')

        computer_choice = random.randint(1, 3)
        while computer_choice == user_choice:
            computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice_str = 'ROCK'
        elif computer_choice == 2:
            computer_choice_str = 'PAPER'
        else:
            computer_choice_str = 'SCISSOR'

        print('Computer choice is', computer_choice_str)
        print(f'{user_choice_str} vs {computer_choice_str}')

        if user_choice == computer_choice:
            print('It\'s a Draw')
            result = 'DRAW'
        elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
            print('Paper wins')
            result = 'PAPER'
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
            print('Rock wins')
            result = 'ROCK'
        else:
            print('Scissors wins')
            result = 'SCISSORS'

        if result == 'DRAW':
            print('<== It\'s a tie ==>')
        elif result == user_choice_str:
            print('<== User wins ==>')
        else:
            print('<== Computer wins ==>')

        play_again = input('Do you want to play again? (Y/N): ').lower()
        if play_again == 'n':
            break

    print('Thanks for playing!')

# Call the play_game function to start the game
play_game()
