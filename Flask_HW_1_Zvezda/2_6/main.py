from flask import Flask, json

app = Flask(__name__)
USER_DB_LINK = r"db.json"


def json_load(db_link: str = USER_DB_LINK) -> dict:
    with open(db_link, "r", encoding="UTF-8-SIG") as f:
        return json.load(f)


USER_DB = json_load()


@app.route(
    "/profile/<string:user_id>",
)
def page_index(user_id) -> str:
    return f"""{user_id} {USER_DB[user_id]["FIO"]} {USER_DB[user_id]["TEL"]}"""


if __name__ == "__main__":
    app.run(debug=True)
