import random
import prompt

from brain_games.common.game_template import run_game


def random_progression(progr_min_lenght: int, progr_max_length: int,
                       progr_min_start: int, progr_max_start: int,
                       progr_min_step: int, progr_max_step: int) -> list:
    '''Принимает параметры: мин/макс длина, мин/макс 1-й член, мин/макс шаг
       и генерирует рандомный фрагмент арифметической прогрессии'''

    # Генерация случайных параметров прогрессии:
    progr_start = random.randint(progr_min_start, progr_max_start)  # 1й член
    progr_length = random.randint(progr_min_lenght, progr_max_length)  # длина
    progr_step = random.randint(progr_min_step, progr_max_step)  # шаг
    progr_end = progr_start + progr_length * progr_step  # последний член

    # Генерация собственно прогрессии
    return [nr for nr in range(progr_start, progr_end, progr_step)]


def question_progression(progr_parameters: tuple) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
       для игры в поиск пропущенного члена арифметической прогрессии'''

    progression = random_progression(*progr_parameters)

    # Генерация индекса "пропавшей" позиции во фрагменте прогрессии: [0:-1]
    missed_idx = random.randint(0, len(progression) - 1)

    correct_answer = progression[missed_idx]  # верный ответ как целое
    progression[missed_idx] = '..'  # подмена "пропавшего" числа

    # вопрос как строка. Числа разделены пробелом
    question = 'Question: ' + ' '.join([str(member) for member in progression])

    return question, correct_answer


def answer_request() -> int:
    ''' Получение ответа пользователя на вопрос попытки'''
    return prompt.integer('Your answer: ')


def progression():
    # Параметры игры
    attempts = 3  # Кол-во попыток
    progr_min_lenght = 5  # длина фрагмента прогреммии минимальная
    progr_max_length = 10  # длина фрагмента прогрессии максимальная
    progr_min_start = 1  # минимальное первое число прогрессии
    progr_max_start = 25  # максимальное первое число прогрессии
    progr_min_step = 2  # минимальный шаг прогрессии
    progr_max_step = 11  # максимальный шаг прогрессии
    # все параметры для формирования прогрессии в одном кортеже
    progr_params = (progr_min_lenght, progr_max_length,
                    progr_min_start, progr_max_start,
                    progr_min_step, progr_max_step)

    task = 'What number is missing in the progression?'

    run_game(task, attempts, answer_request, question_progression,
             (progr_params,))


if __name__ == '__main__':
    progression()
