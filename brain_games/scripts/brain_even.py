#!/usr/bin/env python3


import random
import prompt
from colorama import Fore
import brain_games.cli as cli


def main():
    user_name = cli.welcome_user()  # приветствие, получение имени
    attempts = 3  # Кол-во попыток
    min_number, max_number = 1, 100  # диапазон номеров
    parity = {True: 'yes', False: 'no'}  # четность и варианты ответов

    print('Answer "yes" if the number is even, otherwise answer "no"')

    for attempt in range(attempts):
        number = random.randint(min_number, max_number)  # целое в диапазоне

        print(f'Question: {number}')  # задаем вопрос

        is_even = number % 2 == 0  # True/False если четное/нечетное
        correct_answer = parity[is_even]  # верный ответ (yes/no)
        answer = prompt.string('Your answer: ').lower()  # ответ пользователя

        if answer == correct_answer:    # удачная попытка
            print(Fore.GREEN, 'Correct!', Fore.RESET, sep='')
        else:                           # неудачная попытка
            print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                            f"Correct answer was '{correct_answer}'.\n"
                            f"Let's try again, {user_name}", Fore.RESET, sep='')
            break  # завершение программы в случае неверного ответа
    else:  # если все ответы были верные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET)


if __name__ == '__main__':
    main()
