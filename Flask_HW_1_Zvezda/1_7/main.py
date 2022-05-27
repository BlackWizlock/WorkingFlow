from flask import Flask, json

app = Flask(__name__)
DB_FILE = r"db.json"


def json_load_db(db_name: str = DB_FILE) -> list:
    with open(db_name, "r", encoding="UTF-8-SIG") as f:
        return json.load(f)


@app.route(
    "/",
)
def page_index():
    return " ".join(str(x) for x in json_load_db())


@app.route(
    "/first",
)
def page_first():
    return str(json_load_db()[0])


@app.route(
    "/last",
)
def page_last():
    return str(json_load_db()[-1])


@app.route(
    "/sum",
)
def page_sum():
    return str(sum(json_load_db()))


if __name__ == "__main__":
    app.run(debug=True)
