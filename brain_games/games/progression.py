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

    # Генерация случайных параметров прогрессии:
    progr_start = randint(PROGR_FIRST_MIN, PROGR_FIRST_MAX)  # 1й член
    progr_length = randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)  # длина
    progr_step = randint(PROGR_STEP_MIN, PROGR_STEP_MAX)  # шаг прогрессии
    progr_end = progr_start + progr_length * progr_step  # последний член

    # Генерация собственно прогрессии
    return [nr for nr in range(progr_start, progr_end, progr_step)]


def riddle_and_answer() -> tuple:
    '''Возвращает вопрос и правильный ответ для игры
       в поиск пропущенного члена арифметической прогрессии'''
    progression = random_progression()

    # Генерация индекса пропущенной позиции во фрагменте прогрессии: [0:-1]
    missed_idx = randint(0, len(progression) - 1)

    correct_answer = f'{progression[missed_idx]}'  # верный ответ как строка
    progression[missed_idx] = '..'  # подмена "пропавшего" числа

    # вопрос как строка. Числа разделены пробелом
    riddle = ' '.join([str(member) for member in progression])

    return riddle, correct_answer
