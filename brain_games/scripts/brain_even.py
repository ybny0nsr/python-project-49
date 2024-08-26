#!/usr/bin/env python3


import random
import prompt
from colorama import Fore
import brain_games.cli as cli


def main():
    user_name = cli.welcome_user()
    attempts = 3  # Кол-во попыток
    min_number, max_number = 1, 100  # диапазон номеров
    parity = {True: 'yes', False: 'no'}
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for attempt in range(attempts):
        number = random.randint(min_number, max_number)  # целое в диапазоне
        is_even = number % 2 == 0  # True/False если четное/нечетное
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()  # ответ - в прописные
        correct_answer = parity[is_even]  # правильный ответ
        if answer == parity[is_even]:    # удачная попытка
            print(Fore.GREEN, 'Correct!', Fore.RESET)
        else:                           # неудачная попытка
            print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                            f"Correct answer was '{correct_answer}'.\n"
                            f"Let's try again, {user_name}", Fore.RESET)
            break  # завершение программы
    else:  # если все попытки - удачные
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET)


if __name__ == '__main__':
    main()
