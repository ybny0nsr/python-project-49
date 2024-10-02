from random import randint

# Параметры игры
GAME_CONDITIONS = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1    # Минимальное число для игры
MAX_NUMBER = 100  # Максимальное число для игры


def find_divisors(number: int) -> set:
    '''Возвращает множество делителей целого числа N в диапазоне 1...N
       или {1}, если N = 0 '''
    return set(filter(lambda x: not number % x, range(1, number + 1)))


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ: наибольший общий делитель
    для двух целых в диапазоне 1...max_number'''
    nr_one = randint(MIN_NUMBER, MAX_NUMBER)
    nr_two = randint(MIN_NUMBER, MAX_NUMBER)
    gcd = max(find_divisors(nr_one) & find_divisors(nr_two))
    riddle = f'{nr_one} {nr_two}'
    correct_answer = f'{gcd}'
    return riddle, correct_answer
