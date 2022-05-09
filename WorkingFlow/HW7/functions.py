import json


def load_students(filename: str) -> list:
    """
    Загружает студентов из файла в список
    :param
    filename: Имя файла JSON
    :return:
    возврат словаря JSON
    """
    with open(filename, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def load_professions(filename: str) -> list:
    """
    Загружает навыки из файла в список
    :param
    filename: Имя файла JSON
    :return:
    возврат словаря JSON
    """
    with open(filename, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def get_student_by_pk(pk: int, usr_lst: list):
    """
    Получает словарь с данными студента по его pk
    :param
    pk: порядковый номер - ввод с клавиатуры
    usr_lst: словарь JSON
    :return:
    Возврат строки словаря или False для отработки исключений базы
    """
    for item in usr_lst:
        if item['pk'] == pk:
            return item
    return False


def get_profession_by_title(title: str, usr_lst: list):
    """
    Получает словарь с инфо о профессии по названию
    :param
    title: профессия - ввод с клавиатуры
    usr_lst: словарь JSON
    :return:
    Возврат строки словаря или False для отработки исключений базы
    """
    for item in usr_lst:
        if item['title'] == title:
            return item
    return False


def check_fitness(student: set, profession: set) -> dict:
    """
    Обработка множеств
    :param
    student: множество с информацией по знаниям студента
    profession: множество с информацией по требованию работодателя
    :return:
    возврат словаря с отработкой множеств и сформированной карточкой соискателя
    """
    out_dict = {
        "has": [*student.intersection(profession)],
        "lacks": [*profession.difference(student)],
        "fit_percent": round(len(student.intersection(profession)) / len(profession) * 100)
    }

    return out_dict
