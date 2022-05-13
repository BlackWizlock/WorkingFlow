from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    return "It works"


@app.route('/hello', )
def page_hello():
    return "hello"


@app.route('/goodbye', )
def page_goodbye():
    return "goodbye"


@app.route('/seeyou', )
def page_seeyou():
    return "seeyou"


if __name__ == "__main__":
    app.run(debug=True)
