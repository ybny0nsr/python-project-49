# Установки и настройки
min_number = 1  # диапазон чисел для игры - от ...
max_number = 100  # до ...
attempts = 3  # Кол-во попыток

max_lcd = 9  # вспомогательный параметр для расчета GCD

progr_min_lenght = 5  # длина аврифметической прогреммии минимальная
progr_max_length = 10  # длина арифметической прогрессии максимальная
progr_min_start = 1  # минимальное первое число прогрессии
progr_max_start = 25  # максимальное первое число прогрессии
progr_min_step = 2  # минимальный шаг прогрессии
progr_max_step = 11  # максимальный шаг прогрессии
# полный набор параметров для генерации прогрессии
progr_params = (progr_min_lenght, progr_max_length,
                progr_min_start, progr_max_start,
                progr_min_step, progr_max_step)

task_even = 'Answer "yes" if the number is even, otherwise answer "no"'
task_calc = 'What is the result of the expression?'
task_gcd = 'Find the greatest common divisor of given numbers.'
task_progression = 'What number is missing in the progression?'
