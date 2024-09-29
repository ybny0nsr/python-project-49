import prompt


def name_normalizer(raw_name: str) -> str:
    '''Возвращает аргумент, все слова в котором записаны с большой буквы,
    или "stranger", если в аргументе одни пробелы или None'''
    if raw_name is None or raw_name.strip() == "":
        return "stranger"
    else:
        return " ".join([name.capitalize() for name in raw_name.split()])


def welcome_user():
    '''Спрашивает имя пользователя и выводит приветствие'''
    raw_user_name = prompt.string('May I have your name? ', empty=False)
    print(f'Hello, {name_normalizer(raw_user_name)}!')
