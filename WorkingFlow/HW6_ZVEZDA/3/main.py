import csv


def read_fl(fl_name: str) -> dict:
	"""
	Чтение файла по имени
	Результат: лист данных
	fl_name : имя файла
	"""
	usr_dct = dict()
	with open(fl_name, encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			usr_dct.update({row[0]: row[1].lower()})
	return usr_dct


def main():
	fl_pass = open('passed.txt', 'w', encoding='utf-8')
	fl_fail = open('failed.txt', 'w', encoding='utf-8')
	for name, points in read_fl('db.csv').items():
		if int(points) >= 75:
			fl_pass.write(f'{name}\n')
		else:
			fl_fail.write(f'{name}\n')
	fl_pass.close()
	fl_fail.close()


if __name__ == '__main__':
	main()
