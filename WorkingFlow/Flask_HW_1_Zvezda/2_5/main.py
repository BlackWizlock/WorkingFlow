from flask import Flask, json

app = Flask(__name__)


@app.route(
    "/<string:meal_1>/<string:meal_2>/<string:meal_3>/",
)
def page_index(meal_1: str = None, meal_2: str = None, meal_3: str = None) -> str:
    return f"""<pre>
           На первое: {meal_1}
           На второе: {meal_2}
           На третье: {meal_3}
           </pre>"""


if __name__ == "__main__":
    app.run(debug=True)
