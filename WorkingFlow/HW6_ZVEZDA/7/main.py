def read_file(filename: str):
	lst_file_data = list()
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lst_file_data.append(line.strip())
	return lst_file_data


def show_statistic(phrase: int = 0, words: int = 0, symbols: int = 0):
	print(f'Предложений - {phrase}\n'
		  f'Слов - {words}\n'
		  f'Символов – {symbols}')


def main():
	# user_file_name = str(input('Введите имя файла :'))
	user_file_input = read_file('db.txt')
	words = 0
	phrases = 0
	symbols = 0
	for lines in user_file_input:
		words += len(lines.split(" "))

	for lines in user_file_input:
		for symbol in lines:
			if not symbol.isspace():
				symbols += 1

	show_statistic(words=words, symbols=symbols)
	# print(*user_file_input, sep='\n')


if __name__ == '__main__':
	main()
