def ask_question(question_number, correct_answer, prompt):
    global score
    global ques

    ques += 1
    user_answer = input(f'\n{question_number}. {prompt}: ').lower()

    if user_answer == correct_answer:
        score += 1
        print('Correct! You got 1 point')
    else:
        print('Incorrect!')
        print(f'Correct answer is ---> {correct_answer}')


def play_marvel_quiz():
    print("Welcome to 'HOW BIG MARVEL FAN ARE YOU' quiz")
    print("Few questions will be asked and on the basis of your answers,")
    print("your level will be decided, and an Avenger title will be given to you!!!")

    print('NOTE: If your spelling is incorrect, then it is considered as the wrong answer')

    global score
    global ques
    score = 0
    ques = 0

    play = input('Do you want to play? ').lower()

    if play == 'yes' or play == 'y':
        ask_question(ques + 1, '6', 'How many Infinity Stones are there?')
        ask_question(ques + 1, 'captain america civil war', 'In which movie did Spider-Man make his first appearance in the MCU?')
        ask_question(ques + 1, 'mjolnir', "What is the name of Thor's hammer?")
        ask_question(ques + 1, 'strategic homeland intervention, enforcement and logistics division.', 'What does S.H.I.E.L.D. stand for?')
        ask_question(ques + 1, 'avengers endgame', 'Stan Lee made his final cameo in which Marvel movie?')

    else:
        print('Thank you, you are out of the game.')
        quit()

    print(f'\nNumber of questions is {ques}')
    print(f'Your score is {score}')
    percentage = (score * 100) / ques

    print(f'{percentage}% questions are correct.')

    if percentage >= 85:
        print('You are IRONMAN')
    elif percentage >= 70:
        print('You are CAPTAIN AMERICA')
    elif percentage >= 60:
        print('You are THOR')
    elif percentage >= 50:
        print('You are SPIDERMAN')
    elif percentage >= 40:
        print('You are HAWKEYE')
    elif percentage < 40:
        print('You are HULK')


# Start the quiz
play_marvel_quiz()
