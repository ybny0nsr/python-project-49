import prompt

from brain_games.common.game_template import run_game
from brain_games.games.even import random_number


def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    for d in range(3, int(number ** 0.5) + 1, 2):
        if number % d == 0:
            return False
    return True


def question_prime(min_number: int, max_number: int) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
    для игры с определением простого числа'''
    number = random_number(min_number, max_number)
    if not is_prime(number):  # повышаем вероятность "выпадения" prime - с 25%
        number = random_number(min_number, max_number)  # до примерно 44%

    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'  # правильный ответ
    return question, correct_answer


def answer_request() -> int:
    ''' Получение ответа пользователя на вопрос попытки'''
    return prompt.string('Your answer: ')


def prime():
    # Параметры игры
    min_number = 1  # диапазон чисел для игры - от ...
    max_number = 100  # до ...
    attempts = 3  # Кол-во попыток
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    # передаем в шаблон параметры игры
    run_game(task, attempts, answer_request, question_prime,
             (min_number, max_number))


if __name__ == '__main__':
    prime()
