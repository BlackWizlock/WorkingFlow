from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)

USER_DB = load_candidates_from_json()


@app.route("/")
def main_page():
	users_db_len = len(USER_DB)
	return render_template("list.html", users=USER_DB, users_db_len=users_db_len)


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id: int):
	user = get_candidate(candidate_id, USER_DB)
	return render_template("single.html", user=user)


@app.route("/search/<string:candidate_name>")
def search_page(candidate_name: str):
	user = get_candidates_by_name(candidate_name, USER_DB)
	return render_template("search.html", user=user)


if __name__ == "__main__":
	app.run(debug=True)
