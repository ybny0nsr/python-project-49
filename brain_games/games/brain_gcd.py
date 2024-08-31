#!/usr/bin/env python3


import random
import prompt
from colorama import Fore
import brain_games.cli as cli


def main():
    user_name = cli.welcome_user()
    attempts = 3  # Кол-во попыток
    min_nr, max_nr = 1, 100  # диапазон аргументов
    operations = [['*', lambda a, b: a * b],  # значки операций и
                  ['+', lambda a, b: a + b],  # собственно функции,
                  ['-', lambda a, b: a - b]]  # реализующие операцию
    sign, function = 0, 1  # индексы для значка и для функции операций

    print('Find the greatest common divisor of given numbers.')

    for attempt in range(attempts):
        nr_one = random.randint(min_nr, max_nr)  # генерация 1го аргумента
        nr_two = random.randint(min_nr, max_nr)  # генерация 2го аргумента
        if nr_two > nr_one:  # избегание отрицательных значений при разности
            nr_one, nr_two = nr_two, nr_one

        operation = random.choice(operations)  # случайный выбор операции
        correct_answer = operation[function](nr_one,
                                             nr_two)  # результат операции
        print(f'Question: {nr_one} {operation[sign]} {nr_two}')
        answer = prompt.integer('Your answer: ')

        if answer == correct_answer:  # верный ответ
            print(Fore.GREEN, 'Correct!', Fore.RESET, sep='')
        else:  # неверный ответ
            print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                            f"Correct answer was '{correct_answer}'.\n"
                            f"Let's try again, {user_name}", Fore.RESET,
                  sep='')
            break  # завершение программы при неверном ответе
    else:  # если все ответы верные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET, sep='')


if __name__ == '__main__':
    main()
