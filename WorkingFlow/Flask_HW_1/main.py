# import json
from flask import Flask, json

# глобальная переменная пути к БД
DATABASE_FILE_PATH = r"candidates.json"


def load_students(filename: str = DATABASE_FILE_PATH) -> list:
    """
    Загружает БД из json
    Args:
        filename: Имя файла JSON
    Returns: возврат словаря JSON
    """
    with open(filename, "r", encoding="utf-8-sig") as f:
        return json.load(f)


app = Flask(__name__)  # создаем экземпляр класса Фласк
user_database = load_students()  # инициализация БД


@app.route("/")
def page_index():
    """
    Основная страничка
    """
    output = ""
    for line in user_database:
        output += (
            line["name"]
            + "<br>"
            + line["position"]
            + "<br>"
            + line["skills"]
            + "<br><br>"
        )
    return "<pre>" + output + "</pre>"


@app.route("/json/")
def page_index_json():
    """
    Основная страничка с методом json
    """
    return load_students()[0]


@app.route("/candidates/<string:candidate_name>")
def page_candidates(candidate_name: str):
    """
    Личная страничка кандидата
    Args:
        candidate_name: Имя кандидата из БД
    """
    output = ""
    for line in user_database:
        if line["name"].lower() == candidate_name.lower():
            output += (
                "<img src="
                + line["picture"]
                + "><br><br><pre>"
                + line["name"]
                + "<br>"
                + line["position"]
                + "<br>"
                + line["skills"]
                + "<br><br>"
            )
            break
    return output + "</pre>"


@app.route("/skills/<string:skill_to_search>")
def page_skills(skill_to_search: str):
    """
    Страничка по скиллу
    Args:
        skill_to_search: скилл для поиска в БД
    """
    output = ""
    for line in user_database:
        if skill_to_search.lower() in line["skills"].lower():
            output += (
                line["name"]
                + "<br>"
                + line["position"]
                + "<br>"
                + line["skills"]
                + "<br><br>"
            )
    return "<pre>" + output + "</pre>"


if __name__ == "__main__":
    app.run(debug=True)
