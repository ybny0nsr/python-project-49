import prompt


USER_NAME = 'TBD'


def name_normalizer(raw_name: str) -> str:
    '''Возвращает имена, записанные с заглавной буквы или stranger,
    если в аргументе пробелы или None'''
    if raw_name is None or raw_name.strip() == "":
        return "stranger"
    else:
        return " ".join([name.capitalize() for name in raw_name.split()])
    # TODO распространить на варианты имен с "-"(Newton-John) и "'"(д'Артаньян)


def welcome_user():
    '''Спрашивает имя пользователя и выводит приветствие'''
    global USER_NAME
    raw_user_name = prompt.string('May I have your name? ', empty=False)
    USER_NAME = name_normalizer(raw_user_name)
    print(f'Hello, {USER_NAME}!')


if __name__ == '__main__':
    welcome_user()
