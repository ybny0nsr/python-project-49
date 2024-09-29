import random

# Параметры игры
GAME_CONDITIONS = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100  # Максимальное число для игры
MAX_LCD = 9       # Верхний предел для генерации случайного наименьшего
# общего делителя. Вспомогательный технический параметр для расчета GCD,
# рекомендуется выбирать его значение в диапазоне 9...11


def random_pair_gcd(max_number: int, max_lcd: int) -> tuple:
    '''Возвращает пару случайных целых чисел в диапазоне 1...max_nr,
    имеющих по крайней мере 1 общий целый делитель в диапазоне 1...max_lcd'''
    if max_lcd >= max_number or max_lcd <= 1:
        raise Exception('max_lcd have to be positive and less than max_number')
    lcd = random.randint(1, max_lcd)  # least common divisor
    nr_one = nr_two = random.randrange(lcd, max_number + 1, lcd)
    while nr_one == nr_two:  # исключаем совпадение сгенерированных чисел
        nr_two = random.randrange(lcd, max_number + 1, lcd)
    return nr_one, nr_two


def find_divisors(number: int) -> set:
    '''Возвращает множество делителей целого числа N в диапазоне 1...N
       или {1}, если N = 0 '''
    divisors = {divisor for divisor in range(1, number + 1) if
                number % divisor == 0} if number != 0 else {1}
    return divisors


def find_gcd(nr_one: int, nr_two: int) -> int:
    '''Возвращает максимальный общий делитель для двух целых аргументов'''
    divisors_one = find_divisors(nr_one)  # все делители для 1го аргумента
    divisors_two = find_divisors(nr_two)  # все делители для 2го аргумента
    common_divisors = divisors_one & divisors_two  # только общие делители
    return max(common_divisors)


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ: наибольший общий делитель
    для двух целых в диапазоне 1...MAX_NUMBER'''
    nr_one, nr_two = random_pair_gcd(MAX_NUMBER, MAX_LCD)

    riddle = f'{nr_one} {nr_two}'
    correct_answer = f'{find_gcd(nr_one, nr_two)}'
    return riddle, correct_answer
