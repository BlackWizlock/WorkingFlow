from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


@app.route('/random', )
def page_random():
    return str(randint(0, 10))


if __name__ == "__main__":
    app.run(debug=True)
