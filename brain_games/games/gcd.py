import prompt
from colorama import Fore

import brain_games.cli as cli
import brain_games.common.settings as settings
import brain_games.common.functions as f


def main():
    user_name = cli.welcome_user()  # Приветствие, запрос имени

    print(settings.TASK_GCD)  # сообщаем условия игры

    for attempt in range(settings.ATTEMPTS):
        # генерация вопроса и правильного ответа для этого вопроса
        question, correct_answer = f.question_gcd(settings.MAX_NUMBER,
                                                  settings.MAX_LCD)
        print(question)  # выводим вопрос для текущей попытки

        answer = prompt.integer('Your answer: ')

        check_result = f.feedback(answer, correct_answer, user_name)
        if not check_result:  # ответ неверный, завершаем игру
            break
    else:  # если все попытки удачные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET, sep='')


if __name__ == '__main__':
    main()
