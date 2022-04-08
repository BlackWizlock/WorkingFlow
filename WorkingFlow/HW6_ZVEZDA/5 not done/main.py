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
	start_pos = 2
	current_pos = 2
	f = open('furry_road.txt', 'r', encoding='utf-8')
	for line in f:
		usr_lst = line.strip().split(';')
		while 0 <= current_pos <= 5:
			if usr_lst[start_pos] == '0':
				print('stay')
			if usr_lst[start_pos] == '0':
				print('stay')


if __name__ == '__main__':
	main()
