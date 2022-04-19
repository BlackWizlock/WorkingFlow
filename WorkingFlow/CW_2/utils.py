from requests import get
from random import choice
import classes

# ссылка на JSON БД
URL_DB = r"https://jsonkeeper.com/b/P0AC"


def load_random_word(url: str = URL_DB):
    """подгрузка БД JSON через GET REQUESTS с инициализацией игровых значений, включая рандомный выбор слова из базы

    Args:
        url (str, optional): Ссылка на БД. Defaults to URL_DB.

    Returns:
        _type_: генерация экземпляра класса игрока
    """
    user_db = get(url).json()
    user_db_line = choice(user_db)
    word_game = classes.BasicWord(
        raw_word=user_db_line["word"], lst_word=user_db_line["subwords"]
    )
    return word_game
