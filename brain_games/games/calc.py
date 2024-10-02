from random import randint, choice

# Параметры игры
GAME_CONDITIONS = 'What is the result of the expression?'
MIN_NUMBER = 1    # диапазон чисел для игры - от ...
MAX_NUMBER = 100  # до ...
OPS_SIGNS = ['*', '+', '-']


def calculation(a, b, sign):
    '''Производит над числами a и b арифметическую операцию, знак которой
       содержится в sign: "+", "-" или "*" и возвращает результат операции или
       None, если операция не предусмотрена'''
    arithmetic_operations = {'*': lambda a, b: a * b,
                             '+': lambda a, b: a + b,
                             '-': lambda a, b: a - b}
    if sign in arithmetic_operations:
        return arithmetic_operations[sign](a, b)


def riddle_and_answer() -> tuple:
    '''Возвращает строку-вопрос и правильный ответ для игры-калькулятора'''
    nr_one = randint(MIN_NUMBER, MAX_NUMBER)
    nr_two = randint(MIN_NUMBER, MAX_NUMBER)
    ops_sign = choice(OPS_SIGNS)
    riddle = f'{nr_one} {ops_sign} {nr_two}'
    correct_answer = f'{calculation(nr_one, nr_two, ops_sign)}'
    return riddle, correct_answer
