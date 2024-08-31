import random
from colorama import Fore


# функции для brain_gcd
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
    '''Возвращает множество делителей целого аргумента или {1},
    если аргумент равен 0'''
    divisors = {divisor for divisor in range(1, number + 1) if
                number % divisor == 0} if number != 0 else {1}
    return divisors


def find_gcd(nr_one: int, nr_two: int) -> int:
    '''Возвращает максимальный общий делитель для двух целых аргументов'''
    divisors_one = find_divisors(nr_one)  # все делители для 1го аргумента
    divisors_two = find_divisors(nr_two)  # все делители для 2го аргумента
    common_divisors = divisors_one & divisors_two  # только общие делители
    return max(common_divisors)  # наибольший из общих делителей


def question_gcd(max_number: int, max_lcd: int) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ: наибольший общий делитель
    для двух целых в диапазоне 1...max_number'''
    nr_one, nr_two = random_pair_gcd(max_number, max_lcd)  # , max_lcd)
    correct_answer = find_gcd(nr_one, nr_two)  # верный ответ (GCD для N1 и N2)
    question = f'Question: {nr_one} {nr_two}'  # формулировка вопроса

    return question, correct_answer


# функции для brain_calc
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


# функции для brain_even
def random_number(min_number: int, max_number: int) -> int:
    '''Возвращает целое число в диапазоне min_number...max_number'''
    if min_number >= max_number:
        raise Exception('max_number gave to be > min_number')

    number = random.randint(min_number, max_number)  # целое в диапазоне
    return number


def question_even(min_number: int, max_number: int) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
    для игры с определением четного-нечетного'''
    number = random_number(min_number, max_number)
    question = f'Question: {number}'
    correct_answer = 'yes' if number % 2 == 0 else 'no'  # правильный ответ
    return question, correct_answer


# функции общего применения
def feedback(answer: str, correct_answer: str, user_name: str) -> bool:
    '''Сверка ответа пользователя и правильного ответа
    и вывод сообщения о результате.
    Возвращает True/False если ответ верный/неверный'''
    if answer == correct_answer:  # верный ответ
        print(Fore.GREEN, 'Correct!', Fore.RESET, sep='')
        return True
    else:  # неверный ответ
        print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                        f"Correct answer was '{correct_answer}'.\n"
                        f"Let's try again, {user_name}", Fore.RESET, sep='')
        return False
