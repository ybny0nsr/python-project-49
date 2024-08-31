import prompt
from colorama import Fore

import brain_games.cli as cli
import brain_games.common.settings as settings
import brain_games.common.functions as f


def main():
    user_name = cli.welcome_user()  # приветствие, запрос имени

    print(settings.task_even)  # сообщаем условия игры

    for attempt in range(settings.attempts):
        # генерация вопроса и правильного ответа для жэтого вопроса
        question, correct_answer = f.question_even(settings.min_number,
                                                   settings.max_number)
        print(question)  # выводим вопрос для текущей попытки

        answer = prompt.string('Your answer: ').lower()  # ответ - в прописные

        check_result = f.feedback(answer, correct_answer, user_name)
        if not check_result:  # ответ неверный, завершаем игру
            break
    else:  # если все попытки удачные, выводим поздравление
        print(Fore.GREEN, f'Congratulations, {user_name}!', Fore.RESET, sep='')


if __name__ == '__main__':
    main()
