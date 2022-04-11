from random import shuffle


def line_read(lst: list, fl_name: str):
	with open(fl_name, "r", encoding="utf-8") as file:
		for line in file:
			lst.append(line.strip().lower())


def line_write(name: str, user_points: int, fl_name: str):
	with open(fl_name, "a", encoding="utf-8") as file:
		file.write(f'{name} {user_points}\n')


def lst_shuffler(usr_str: str) -> str:
	lst = list(usr_str)
	shuffle(lst)
	return ''.join(lst)


def point_counter(usr_answer: str, item: str) -> bool:
	if usr_answer == item:
		return True
	return False


def show_statistics(fl_name: str) -> tuple:
	game_counter = 0
	max_pts = 0
	champ_name = str()
	with open(fl_name, "r", encoding="utf-8") as file:
		for line in file:
			game_counter += 1
			name_tmp, pts = line.strip().split()
			if max_pts <= int(pts):
				max_pts = int(pts)
				champ_name = name_tmp
	return game_counter, max_pts, champ_name


def main():
	usr_list = list()
	user_points = 0
	name = input("Введите ваше имя :\t").title()
	line_read(usr_list, "words.txt")
	for item in usr_list:
		print(f'Угадай слово :\t {lst_shuffler(item)}')
		usr_answer = str(input(">>> :\t")).lower()
		if point_counter(usr_answer, item):
			print("Верно! Вы получаете 10 очков.")
			user_points += 10
		else:
			print(f"Неверно! Верный ответ – {item}.")
	line_write(name, user_points, "history.txt")
	game_counter, max_pts, champ_name = show_statistics("history.txt")
	print(f'Всего игр сыграно: {game_counter}\nНаш рекордсмен: {champ_name}\nМаксимальный рекорд: {max_pts}')


if __name__ == '__main__':
	main()
