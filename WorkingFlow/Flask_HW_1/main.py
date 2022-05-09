import json
from flask import Flask

# глобальная переменная пути к БД
DATABASE_FILE_PATH = r"candidates.json"


def load_students(filename: str = DATABASE_FILE_PATH) -> list:
    """
    Загружает БД из json
    Args:
        filename: Имя файла JSON
    Returns: возврат словаря JSON
    """
    with open(filename, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


app = Flask(__name__)  # создаем экземпляр класса Фласк
user_database = load_students()  # инициализация БД


@app.route('/')
def page_index():
    """
    Основная страничка
    """
    output = ""
    for line in user_database:
        output += line["name"] + "<br>" + line["position"] + "<br>" + line["skills"] + "<br><br>"
    return "<pre>" + output + "</pre>"


@app.route('/candidates/<string:x>')
def page_candidates(x: str):
    """
    Личная страничка кандидата
    Args:
        x: Имя кандидата из БД
    """
    output = ""
    for line in user_database:
        if line["name"].lower() == x.lower():
            output += "<img src=" + line["picture"] + "><br><br><pre>" + line["name"] + "<br>" + line[
                "position"] + "<br>" + line["skills"] + "<br><br>"
            break
    return output + "</pre>"


@app.route('/skills/<string:x>')
def page_skills(x: str):
    """
    Страничка по скиллу
    Args:
        x: скилл для поиска в БД
    """
    output = ""
    for line in user_database:
        if x.lower() in line["skills"].lower():
            output += line["name"] + "<br>" + line["position"] + "<br>" + line["skills"] + "<br><br>"
    return "<pre>" + output + "</pre>"


if __name__ == "__main__":
    app.run(debug=True)
