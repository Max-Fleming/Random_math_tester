import os
import random

operators = ('+', '-', '*', '/')
correct = list()
answer = ''
pointsEarned = 0
pointsTotal = 0
runApp = 'y'

while runApp == 'y':
    os.system('cls')

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    sign = random.choice(operators)

    pointsTotal += 1

    if sign == '+':
        answer = (number1 + number2)

    elif sign == '-':
        answer = (number1 - number2)

    elif sign == '*':
        answer = (number1 * number2)

    else:
        answer = (number1 / number2)
        answer = round(answer, 3)

    print(f' {"Random Math Problem Generator": ^30} \n\n')
    enteredAnswer = input(f'Problem {pointsTotal}: {number1} {sign} {number2} = ')

    if enteredAnswer == str(answer):
        print('\nCorrect!')
        pointsEarned += 1
        correct.append(enteredAnswer)

    else:
        print(f'Incorrect. Correct answer is {answer}')

    print()
    print(f'Points Earned: {pointsEarned} out of {pointsTotal} Average: {pointsEarned / pointsTotal * 100: .2f}')

    runApp = input('\n\nNext Question? Enter (y/n). ').casefold()

print(f'\n\nYou scored {pointsEarned} out of {pointsTotal} and got the following right:')

for ans in correct:
    print(f'{ans}')
