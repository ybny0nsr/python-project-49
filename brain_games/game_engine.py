from colorama import Fore
import prompt


# Параметры игры
NUMBER_OF_ATTEMPTS = 3  # количество попыток в игре


def perform_func(func, *args):
    ''' Вспомогательная функция, вызыввает переданную в аргументе функцию
        и возвращает ее результат'''
    return func(*args)


def welcome_user():
    '''Спрашивает имя пользователя и выводит приветствие'''
    raw_user_name = prompt.string('May I have your name? ', empty=False)
    user_name = " ".join([name.capitalize() for name in raw_user_name.split()])
    print(f'Hello, {user_name}!')
    return user_name


def run_game(game_module):
    ''' Принимает на вход модуль игры и реализует логику игры
        по единому шаблону.'''

    user_name = welcome_user()  # запрос имени пользователя, приветствие

    print(game_module.GAME_CONDITIONS)  # объявляем условия игры

    for attempt in range(NUMBER_OF_ATTEMPTS):
        # генерация вопроса и правильного ответа для этого вопроса
        riddle, correct_answer = game_module.riddle_and_answer()

        print(f'Question: {riddle}')  # выводим вопрос для текущей попытки

        answer = prompt.string('Your answer: ').lower()

        # Сверка ответа пользователя и правильного ответа
        if answer == correct_answer:  # верный ответ, продолжаем игру
            print(Fore.GREEN, "Correct!", Fore.RESET, sep='')
        else:  # неверный ответ
            print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                            f"Correct answer was '{correct_answer}'.\n"
                            f"Let's try again, {user_name}!", Fore.RESET,
                  sep='')
            break  # ответ неверный, завершаем игру
    else:          # все ответы - верные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET,
              sep='')
