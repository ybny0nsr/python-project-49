from random import randint

# Параметры игры
GAME_CONDITIONS = 'Answer "yes" if given number is prime. '\
                  'Otherwise answer "no".'
MIN_NUMBER = 1  # диапазон чисел для игры - от ...
MAX_NUMBER = 100  # до ...


def is_prime(number: int) -> bool:
    ''' Один из канонических алгоритмов проверки, является ли число простым'''
    if number == 2:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    for d in range(3, int(number ** 0.5) + 1, 2):
        if number % d == 0:
            return False
    return True


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
    для игры с определением простого числа'''
    number = randint(MIN_NUMBER, MAX_NUMBER)  # Генерируем случайное число
    if not is_prime(number):  # и повышаем вероятность "выпадения" prime,
        number = randint(MIN_NUMBER, MAX_NUMBER)  # с 25% до примерно 44%

    riddle = f'{number}'
    correct_answer = 'yes' if is_prime(number) else 'no'  # правильный ответ
    return riddle, correct_answer
