from flask import json
import os

PATH_TO_USER_DB = r'./db/candidates.json'


def load_candidates_from_json(path: str = PATH_TO_USER_DB) -> list:
	""" Возвращает список всех кандидатов """
	with open(os.path.join(os.path.dirname(__file__), path), 'r', encoding="UTF-8-SIG") as f:
		return json.load(f)


def get_candidate(candidate_id: int, user_db: list) -> dict:
	""" Возвращает одного кандидата по его id """
	for line in user_db:
		if candidate_id == line["id"]:
			return line


def get_candidates_by_name(candidate_name: str, user_db: list) -> dict:
	""" Возвращает кандидатов по имени """
	for line in user_db:
		if candidate_name.strip().lower() == line["name"].strip().lower():
			return line


def get_candidates_by_skill(skill_name: str, user_db: list):
	""" Возвращает кандидатов по навыку """
	output_users_with_skill = []
	for line in user_db:
		if skill_name.strip().lower() in line["skills"].lower().split(", "):
			output_users_with_skill.append(line)
	return output_users_with_skill
