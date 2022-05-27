from flask import Flask, json

app = Flask(__name__)
RECORDS = []


@app.route(
    "/",
)
def page_index():
    return " "


@app.route(
    "/add/<string:word>/",
)
def page_add(word):
    RECORDS.append(word)
    return f"Слово: {word} добавлено"


@app.route(
    "/show/",
)
def page_show():
    return " ".join(RECORDS)


if __name__ == "__main__":
    app.run(debug=True)
