import random
import prompt


from brain_games.common.game_template import run_game


def random_number(min_number: int, max_number: int) -> int:
    '''Возвращает целое число в диапазоне min_number...max_number'''
    if min_number >= max_number:
        raise Exception('max_number have to be > than min_number')
    number = random.randint(min_number, max_number)  # целое в диапазоне
    return number


def question_even(min_number: int, max_number: int) -> tuple:
    '''Возвращает строку-вопрос и правильный ответ
    для игры с определением четного-нечетного'''
    number = random_number(min_number, max_number)
    question = f'Question: {number}'
    correct_answer = 'yes' if number % 2 == 0 else 'no'  # правильный ответ
    return question, correct_answer


def answer_request() -> str:
    ''' Получение ответа пользователя на вопрос попытки'''
    return prompt.string('Your answer: ').lower()


def even():
    # Параметры игры
    min_number = 1  # диапазон чисел для игры - от ...
    max_number = 100  # до ...
    attempts = 3  # Кол-во попыток
    task = 'Answer "yes" if the number is even, otherwise answer "no".'

    # передаем в шаблон параметры игры
    run_game(task, attempts, answer_request, question_even,
             (min_number, max_number))


if __name__ == '__main__':
    even()
