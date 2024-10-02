from random import randint

# Параметры игры
GAME_CONDITIONS = 'What number is missing in the progression?'
PROGR_FIRST_MIN = 1  # минимальное первое число прогрессии
PROGR_FIRST_MAX = 25  # максимальное первое число прогрессии
PROGR_LENGTH_MIN = 5  # длина фрагмента прогрессии (минимальная)
PROGR_LENGTH_MAX = 10  # длина фрагмента прогрессии (максимальная)
PROGR_STEP_MIN = 2  # минимальный шаг прогрессии
PROGR_STEP_MAX = 11  # максимальный шаг прогрессии


def random_progression() -> list:
    '''Генерирует рандомный фрагмент арифметической прогрессии'''
    progr_first = randint(PROGR_FIRST_MIN, PROGR_FIRST_MAX)
    progr_length = randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)
    progr_step = randint(PROGR_STEP_MIN, PROGR_STEP_MAX)
    progr_last = progr_first + progr_step * progr_length
    return list(range(progr_first, progr_last, progr_step))


def riddle_and_answer() -> tuple:
    '''Возвращает вопрос и правильный ответ для игры
       в поиск пропущенного члена арифметической прогрессии'''
    progression = random_progression()
    missed_idx = randint(0, len(progression) - 1)
    correct_answer = f'{progression[missed_idx]}'
    progression[missed_idx] = '..'
    riddle = ' '.join([str(member) for member in progression])
    return riddle, correct_answer
