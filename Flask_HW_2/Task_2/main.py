from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__)

USER_DB = load_candidates_from_json()


@app.route("/")
def main_page():
	return render_template("list.html", users=USER_DB, users_db_len=len(USER_DB))


@app.route("/candidate/<int:candidate_id>")
def candidate_page(candidate_id: int):
	return render_template("single.html", user=get_candidate(candidate_id, USER_DB))


@app.route("/search/<string:candidate_name>")
def search_page(candidate_name: str):
	search_result = get_candidates_by_name(candidate_name, USER_DB)
	return render_template("search.html", search_result=search_result, search_result_amount=len(search_result))


@app.route("/skill/<string:skill_name>")
def search_skill(skill_name: str):
	search_result = get_candidates_by_skill(skill_name, USER_DB)
	return render_template("skill.html", search_result=search_result, skill_name=skill_name,
						   search_result_amount=len(search_result))


if __name__ == "__main__":
	app.run(debug=True)
