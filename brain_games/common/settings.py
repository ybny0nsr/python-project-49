# Установки и настройки
MIN_NUMBER = 1  # диапазон чисел для игры - от ...
MAX_NUMBER = 100  # до ...
ATTEMPTS = 3  # Кол-во попыток

MAX_LCD = 9  # вспомогательный параметр для расчета GCD

PROGR_MIN_LENGTH = 5  # длина аврифметической прогреммии минимальная
PROGR_MAX_LENGTH = 10  # длина арифметической прогрессии максимальная
PROGR_MIN_START = 1  # минимальное первое число прогрессии
PROGR_MAX_START = 25  # максимальное первое число прогрессии
PROGR_MIN_STEP = 2  # минимальный шаг прогрессии
PROGR_MAX_STEP = 11  # максимальный шаг прогрессии

# полный набор параметров для генерации прогрессии
PROGR_PARAMS = (PROGR_MIN_LENGTH, PROGR_MAX_LENGTH,
                PROGR_MIN_START, PROGR_MAX_START,
                PROGR_MIN_STEP, PROGR_MAX_STEP)

# формулировки заданий для игры
TASK_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
TASK_CALC = 'What is the result of the expression?'
TASK_GCD = 'Find the greatest common divisor of given numbers.'
TASK_PROGRESSION = 'What number is missing in the progression?'
TASK_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
