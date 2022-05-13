from flask import Flask, request, render_template
from random import randint

user_list = [23, 16, 144, 72, 90, 11, 5]
app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


@app.route('/first', )
def page_first():
    return str(user_list[0])


@app.route('/last', )
def page_last():
    return str(user_list[-1])


@app.route('/sum', )
def page_sum():
    return str(sum(user_list))


if __name__ == "__main__":
    app.run(debug=True)
