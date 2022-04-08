def read_fl(fl_name: str) -> list:
	"""
	Чтение файла по имени
	Результат: лист данных
	fl_name : имя файла
	"""
	usr_lst = list()
	with open(fl_name, 'r', encoding='utf-8') as f:
		for line in f:
			usr_lst.append(line.strip())
	return usr_lst


def main():
	usr_search_str = str(input()).strip().lower()
	usr_msg_fl = read_fl('messages.txt')
	fnd_cnt = 0
	for line in usr_msg_fl:
		if line.find(usr_search_str) >= 0:
			fnd_cnt += 1
	print(f'Ищем: {usr_search_str}')
	if fnd_cnt > 0:
		print(f'Найдено сообщений {fnd_cnt}')
	else:
		print(f'Сообщений не найдено')


if __name__ == '__main__':
	main()
