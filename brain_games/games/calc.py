import random
import prompt


from brain_games.common.game_template import run_game


def random_pair_calc(min_number: int, max_number: int) -> tuple:
    '''Возвращает пару целых чисел в диапазоне min_number...max_number'''
    if min_number >= max_number:
        raise Exception('min_number have to be < max_number')

    nr_one = random.randint(min_number, max_number)  # генерация 1-го аргумента
    nr_two = random.randint(min_number, max_number)  # генерация 2-го аргумента
    if nr_two > nr_one:  # избегание отрицательных значений при разности
        nr_one, nr_two = nr_two, nr_one
    return nr_one, nr_two


def question_calc(min_number: int, max_number: int) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ для игры-калькулятора'''
    operations = [['*', lambda a, b: a * b],  # значки операций и
                  ['+', lambda a, b: a + b],  # собственно функции,
                  ['-', lambda a, b: a - b]]  # реализующие операцию
    sign, function = 0, 1  # индексы для значка операции и для самой операции

    nr_one, nr_two = random_pair_calc(min_number, max_number)
    operation = random.choice(operations)  # случайный выбор операции
    correct_answer = operation[function](nr_one, nr_two)  # результат операции
    question = f'Question: {nr_one} {operation[sign]} {nr_two}'  # вопрос

    return question, correct_answer


def answer_request() -> int:
    ''' Получение ответа пользователя на вопрос попытки'''
    return prompt.integer('Your answer: ')


def calc():
    # Параметры игры
    min_number = 1  # диапазон чисел для игры - от ...
    max_number = 100  # до ...
    attempts = 3  # Кол-во попыток
    task = 'What is the result of the expression?'

    # передаем в шаблон параметры игры
    run_game(task, attempts, answer_request, question_calc,
             (min_number, max_number))


if __name__ == '__main__':
    calc()
