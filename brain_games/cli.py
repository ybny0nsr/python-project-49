import prompt


def name_normalizer(raw_name: str) -> str:
    '''Возвращает имена, записанные с заглавной буквы или "stranger",
    если в аргументе только пробелы или None'''
    if raw_name is None or raw_name.strip() == "":
        return "stranger"
    else:
        return " ".join([name.capitalize() for name in raw_name.split()])
    # TODO распространить на варианты имен с "-"(Newton-John) и "'"(д'Артаньян)


def welcome_user():
    '''Спрашивает имя пользователя и выводит приветствие'''
    raw_user_name = prompt.string('May I have your name? ', empty=False)
    user_name = name_normalizer(raw_user_name)
    print(f'Hello, {user_name}!')


if __name__ == '__main__':
    welcome_user()
