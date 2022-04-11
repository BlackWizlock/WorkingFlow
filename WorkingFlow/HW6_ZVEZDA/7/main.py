import re

pattern_phrases = r'[.!?;:]\s+[A-ZА-Я]'
pattern_words = r'\w+'
pattern_symbols = r'\S'


def read_file(filename: str):
	lst_file_data = list()
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lst_file_data.append(line.strip())
	return " ".join(lst_file_data)


def show_statistic(phrase: int = 0, words: int = 0, symbols: int = 0):
	print(f'Предложений - {phrase}\n'
		  f'Слов - {words}\n'
		  f'Символов – {symbols}')


def main():
	user_file_input = read_file('db.txt')
	words = len(re.findall(pattern_words, user_file_input))
	phrases = len(re.findall(pattern_phrases, user_file_input)) + 1
	symbols = len(re.findall(pattern_symbols, user_file_input))
	show_statistic(words=words, symbols=symbols, phrase=phrases)


if __name__ == '__main__':
	main()
