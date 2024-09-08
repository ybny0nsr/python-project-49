import random
import prompt


from brain_games.common.game_template import run_game


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
    '''Возвращает множество делителей целого числа в диапазоне 1...число
       или {1}, если аргумент равен 0'''
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


def answer_request() -> int:
    ''' Получение ответа пользователя на вопрос попытки'''
    return prompt.integer('Your answer: ')


def gcd():
    # Параметры игры
    max_number = 100  # Максимальное число для игры
    attempts = 3  # Кол-во попыток
    max_lcd = 9  # верхний предел для генерации случайного наименьшего общего
    # делителя. Вспомогательный параметр для расчета GCD, рекомендуется 9...11
    task = 'Find the greatest common divisor of given numbers.'

    # передаем в шаблон параметры игры
    run_game(task, attempts, answer_request, question_gcd,
             (max_number, max_lcd))


if __name__ == '__main__':
    gcd()
