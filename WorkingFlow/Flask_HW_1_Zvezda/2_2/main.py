from flask import Flask, json

app = Flask(__name__)
USER_DB = {1: "Самара", 2: "Краснодар", 3: "Сочи", 4: "Новосибирск", 5: "Вышгород"}


@app.route(
    "/",
)
def page_index():
    return " "


@app.route(
    "/city/<int:number>/",
)
def page_city(number):
    return USER_DB[number]


if __name__ == "__main__":
    app.run(debug=True)
