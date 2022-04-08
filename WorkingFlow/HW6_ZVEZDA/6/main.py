def read_file(filename: str):
	lst_file_data = list()
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lst_file_data.append(line.strip().split(": "))
	return lst_file_data


def write_file(filename: str, usr_list: list):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in usr_list:
			f.write(f'{line[0]}: {line[1]}\n')


def done_counter(lst_file_data: list) -> int:
	cnt = 0
	for line in lst_file_data:
		if line.count('DONE') != 0:
			cnt += 1
	return cnt


def main():
	lst_file_data = read_file('todo.txt')
	print(f'В списке {len(lst_file_data)} дел\n'
		  f'Сделано {done_counter(lst_file_data)}\n'
		  f'Давай пройдемся по твоим делам!\n')
	for line in lst_file_data:
		if line[1] == 'TODO':
			usr_answer = str()
			while usr_answer not in ('y','n'):
				usr_answer = input(f'{line[0]} - сделано? (y/n)\t').lower()
				if usr_answer == "y":
					line[1] = "DONE"
				elif usr_answer == 'n':
					break
	write_file('todo.txt', lst_file_data)


if __name__ == '__main__':
	main()
