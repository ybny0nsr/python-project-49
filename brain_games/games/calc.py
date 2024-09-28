from random import randint, choice

# Параметры игры
GAME_CONDITIONS = 'What is the result of the expression?'
MIN_NUMBER = 1    # диапазон чисел для игры - от ...
MAX_NUMBER = 100  # до ...
OPERATIONS = [['*', lambda a, b: a * b],  # значки операций и собственно
              ['+', lambda a, b: a + b],  # функции, реализующие операцию
              ['-', lambda a, b: a - b]]
OPS_SIGN = 0      # индекс для значка операции
OPS_FUNC = 1  # индекс для функции, реализующей операцию


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ для игры-калькулятора'''

    nr_one = randint(MIN_NUMBER, MAX_NUMBER)  # генерация 1-го аргумента
    nr_two = randint(MIN_NUMBER, MAX_NUMBER)  # генерация 2-го аргумента
    if nr_two > nr_one:  # избегаем отрицательной разности в результате
        nr_two, nr_one = nr_one, nr_two

    operation = choice(OPERATIONS)  # случайный выбор операции
    riddle = f'{nr_one} {operation[OPS_SIGN]} {nr_two}'  # вопрос
    correct_answer = f'{operation[OPS_FUNC](nr_one, nr_two)}'  # результат

    return riddle, correct_answer
