# Write your Own Multiplication Quiz Page 199 Chapter 8
import random
import time
import re

def get_user_input(prompt, answer, time_limit=8, max_attempts=3):
    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        user_answer = input(prompt)
        if time.time() - start_time > time_limit:
            print("Out of time!")
            break

        if re.match(r'^\d+$', user_answer):
            user_answer = int(user_answer)
            if user_answer == answer:
                print("Correct!")
                return True
            else:
                print("Incorrect!")
                attempts += 1
        else:
            print("Please enter a valid number.")

    return False

def main():
    numberOfQuestions = 10
    correctAnswers = 0

    for questionNumber in range(1, numberOfQuestions + 1):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        answer = num1 * num2
        prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

        if get_user_input(prompt, answer):
            correctAnswers += 1

        if questionNumber < numberOfQuestions:
            time.sleep(1)

    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

if __name__ == "__main__":
    main()
