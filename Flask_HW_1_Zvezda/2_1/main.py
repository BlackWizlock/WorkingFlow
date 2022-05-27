from flask import Flask, json

app = Flask(__name__)
TEXT_TO_CHECK = """
На крыльце сидел котейка
Мимо шел казах Андрейка
Будет завтра у Андрейки
из котейки тюбетейка
"""


@app.route(
    "/",
)
def page_index():
    return " "


@app.route(
    "/find/<string:word>/",
)
def page_find(word):
    if word in TEXT_TO_CHECK.strip("\n").split():
        return "Да"
    return "Нет"


if __name__ == "__main__":
    app.run(debug=True)
