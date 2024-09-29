from random import randint

# Параметры игры
GAME_CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1    # диапазон чисел для игры - от ...
MAX_NUMBER = 100  # до ...


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
    для игры с определением четного-нечетного'''
    number = randint(MIN_NUMBER, MAX_NUMBER)

    riddle = f'{number}'
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return riddle, correct_answer
