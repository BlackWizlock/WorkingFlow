from flask import Flask, request, render_template
from random import randint
import re

content = "Кот это не хлеб, подумай, не ешь его, разработчик! Ай, ну я же просил"
app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


@app.route('/words', )
def page_words():
    return str(len(re.findall(r"\w+", content)))


@app.route('/spaces', )
def page_spaces():
    return str(len(re.findall(r"\s", content)))


@app.route('/letters', )
def page_letters():
    return str(len(re.findall(r"\w", content)))


if __name__ == "__main__":
    app.run(debug=True)
