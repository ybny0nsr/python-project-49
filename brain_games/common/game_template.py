from colorama import Fore

import brain_games.cli as cli


def perform_func(func, *args):
    ''' Вспомогательная функция, вызыввает переданную в аргументе функцию
        и возвращает ее результат'''
    return func(*args)


def run_game(task: str, attempts: int, answer_request_func, gen_question_func,
             args):
    ''' Реализует логику игры по единому шаблону.
        Принимает на вход
        - формулировку условий игры
        - кол-во попыток
        - функцию запроса ввода ответа пользователем
        - функцию генерации вопроса и правильного ответа и
        - аргументы для нее (кортеж)'''

    cli.welcome_user()  # получение имени пользователя, приветствие
    print(task)  # сообщаем условия игры

    for attempt in range(attempts):
        # генерация вопроса и правильного ответа для этого вопроса
        # question, correct_answer = f.question_even(settings.min_number,
        #                                          settings.max_number)
        question, correct_answer = perform_func(gen_question_func, *args)

        print(question)  # выводим вопрос для текущей попытки

        answer = perform_func(answer_request_func)  # ответ - в прописные

        # Сверка ответа пользователя и правильного ответа
        if answer == correct_answer:  # верный ответ, продолжаем игру
            print(Fore.GREEN, "Correct!", Fore.RESET, sep='')
        else:  # неверный ответ
            print(Fore.RED, f"'{answer}' is wrong answer ;(. "
                            f"Correct answer was '{correct_answer}'.\n"
                            f"Let's try again, {cli.USER_NAME}!", Fore.RESET,
                  sep='')
            break  # ответ неверный, завершаем игру
    else:  # все ответы - верные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {cli.USER_NAME}!', Fore.RESET,
              sep='')
