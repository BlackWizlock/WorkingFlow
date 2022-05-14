from flask import Flask, request, render_template
from random import randint

words = ["@кот", "@хлеб", "не", "ешь", "@подумай", "теперь", "ешь"]
app = Flask(__name__)


@app.route(
    "/",
)
def page_index():
    return "It works"


@app.route(
    "/mentions",
)
def page_mentions():
    return " ".join([i[1::] for i in words if i[0] == "@"])


if __name__ == "__main__":
    app.run(debug=True)
