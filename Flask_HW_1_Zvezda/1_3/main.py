from flask import Flask, request, render_template
from random import randint

words = {"one": "один", "two": "два", "three": "три"}
app = Flask(__name__)


@app.route(
    "/",
)
def page_index():
    return "It works"


@app.route(
    "/<string:string_number>",
)
def page_number(string_number):
    return words[string_number]


if __name__ == "__main__":
    app.run(debug=True)
