""" Mini-game guess the number.
User needs to guess random number from entered range and number of attempts.
"""

import random, sys


attempt_number = 0  # attempt counter
incorrect_answers = []  # list for storage wrong answers

def main():
    minimal, maximum, attempts = get_params()
    guess = random.randint(minimal, maximum)
    print(f"You have {attempts} attempt(s)")
    while attempts >= attempt_number:
        answer = get_answer(minimal, maximum, attempts)
        check_answer(answer, guess, attempts)


def get_params():
    """ Function gets from user each parameters for mini-game with check for integer input: minimal number, maximal number and number of attempts.
    Maximal number couldn't be less or equal minimal number. Number of attempts could be from 1 to difference between maximal and minimal numbers."""

    def get_min():
        while True:
            try:
                return int(input("Minimal number: "))
            except ValueError:
                print("Wrong number")
                continue
    def get_max(min):
        while True:
            try:
                maximum = int(input("Maximum number: "))
                if maximum <= min:
                    print(f"Maximum must be more than minimum '{min}'")
                else:
                    return maximum
            except ValueError:
                print("Wrong number")
                continue
    def get_attempts(min, max):
        while True:
            try:
                attempts = int(input("Attempts number: "))
                if attempts > (max - min):
                    print(f"Number of attempts can't be more than result of maximum and minimum numbers '{max - min}'")
                    continue
                elif attempts < 1:
                    print("Number of attempts can't be less than 1")
                    continue
                else:
                    return attempts
            except ValueError:
                print("Wrong number")
                continue

    minimal = get_min()
    maximum = get_max(minimal)
    attempts = get_attempts(minimal, maximum)
    return minimal, maximum, attempts


def get_answer(minimal, maximum, attempts):
    """ Function gets answer from user with check for integer and with number of attempts remaining."""
    
    global attempt_number
    while True:
        try:
            answer = int(input(f"Choose number from {minimal} to {maximum}: "))
            if answer < minimal or answer > maximum:
                print(f"Outside of the limit values, {attempts-attempt_number} attempt(s) left")
                continue
            else:
                return answer
        except ValueError:
            attempt_number += 1
            if attempt_number < attempts:
                print(f"That's not number, {attempts-attempt_number} attempt(s) left")
            else:
                sys.exit("Game over.")
            continue


def check_answer(answer, guess, attempts):
    """Function checks answers with number of attempts remaining.
    Storage wrong answers and output info if wrong answer was inputted again. In this case attempt not uses."""
    
    global attempt_number, incorrect_answers
    if (attempts - attempt_number) > 1:
        if answer != guess:
            if answer in incorrect_answers:
                print(f"Answer '{answer}' already was. {attempts-attempt_number} attempt(s) left")
            else:
                attempt_number += 1
                print(f"Nope, {attempts-attempt_number} attempt(s) left")
                incorrect_answers.append(answer)
        else:
            sys.exit("That's right. Congratulations!")
    else:
        if answer != guess:
            sys.exit("Game over.")
        else:
            sys.exit("That's right. Congratulations!")


if __name__ == "__main__":
    main()