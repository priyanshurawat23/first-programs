print("welcome to 'HOW BIG MARVEL FAN ARE YOU' quiz\nfew questions will be asked and on basis of your answer"
      +"your level will be decided and an avenger title will be given to you!!!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
ques = 0
play = input('Do you want to play ? ').lower()
if play == 'yes'or 'y':
    ques += 1
    question = input(f'\n{ques}. How many Infinity Stones are there?: ').lower()
    if question == '6' or 'six':
        score +=1
        print('correct! you got 1 point')
    else:
        print('INCORRECT')
        print('correct ans is---> six')

    ques += 1
    question = input(f'\n{ques}. In which movie did Spider-Man make his first appearance in the MCU?: ').lower()

    if question == 'captain america civil war'or 'civil war':
        score += 1
        print('correct! you got +1 point')

    else:
        print('Incorrect!')
        print('correct answer is --> captain america: civil war')

    ques += 1
    question = input(f"\n{ques}. What is the name of thor's hammer?: ").lower()

    if question == 'mjolnir':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print('correct answer is----> mjolnir')

    ques += 1
    question = input(f'\n{ques}. What does S.H.I.E.L.D. stand for?: ').lower()

    if question == 'Strategic Homeland Intervention, Enforcement and Logistics Division.':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print('correct anwer is----> Strategic Homeland Intervention, Enforcement and Logistics Division.')

    ques += 1
    question = input(f'\n{ques}. Stan Lee made his final cameo in which Marvel movie?: ').lower()

    if question == 'endgame'or 'Endgame'or 'avengers endgame:
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print('correct answer is----> avengers endgame')

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {ques}')
print(f'your score is {score}')
percentage = (score *100)/ques


print(f'{percentage}% questions are correct.')

if percentage>=85:
    print('you are IRONMAN')
elif percentage>=70:
    print('you are CAPTAIN AMERICA')
elif percentage>=60:
    print('you are THOR')
elif percentage>=50:
    print('you are SPIDERMAN')
elif percentage>=40:
    print('you are HAWKEYE')
elif percentage<40:
    print('you are HULK')
