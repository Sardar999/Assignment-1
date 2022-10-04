import time
import random

correct = int(0)
count = int(0)
totalquestions = int(5)
while True:
    starttime = time.time()
    print('The quiz has started')


    while count < totalquestions:


        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        rightanswer = num1,num2
        answer = (input(f'What is {num1}  {num2}?: '))

        if answer == 'N' or answer == 'stop' or answer == 'exit':
            break

        answer = int(answer)

        if answer == rightanswer:
            print('You are correct!')
            count += 1
            correct += 1
        elif answer != rightanswer:
            print(f'You are wrong! The right answer is {rightanswer}')
            count += 1
        else:
            print('Invalid answer')
            count += 1

    endtime = time.time()
    totaltime = int(endtime - starttime)

    print(f'The number of points received are {correct} out of {totalquestions}')
    print(f'You finished the quiz in {totaltime} secs')
    print('')
    retake = input('Do you want to retake the quiz? Type Y/N: ')
    if retake == 'Y' or 'y':
        continue
    elif retake == 'N' or retake == "n" or retake == 'stop' or retake == 'exit':
        print("goodbye")
        break
