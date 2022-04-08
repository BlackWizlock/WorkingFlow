from bs4 import BeautifulSoup
from requests import get
import csv
import random

url = r'https://www.usingenglish.com/quizzes/29.html'
HEADERS = {
		'accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36'
}


def get_urs(url, params=''):
	r = get(url, headers=HEADERS, params=params)
	return r.text  # возвращаем HTML странички


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='card slimline card-body mb-3')
	questions = []
	count = 1
	for item in items:
		questions.append(
				{
						'id':             str(count),
						'question':       item.find('div', class_='qheader').get_text(strip=True),
						'answer1':        item.find('label', attrs={'for': f'question{count}0'}).find(
								'strong').get_text(strip=True),
						'answer2':        item.find('label', attrs={'for': f'question{count}1'}).find(
								'strong').get_text(strip=True),
						'correct_answer': 'correct answer here',
				}
		)  # получили лист словарей [{},{}]
		count += 1
	print(f'>> DataBase Status: Created and Stored - {count - 1} elements in DB')
	return questions


def csv_writer(data, filename: str):
	with open(filename, 'w', newline='') as f:
		fieldnames = ["id", "question", "answer1", "answer2", "correct_answer"]
		writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
		writer.writeheader()
		for d in data:
			writer.writerow(d)

	print(f'>> DataBase Status: Re-Wrote as CSV file with name {filename}')


def game_loop():
	db = list(csv.DictReader(open('db_out.csv')))
	question_cnt = int(input('Enter amount of questions in game:\t'))
	for counter in range(question_cnt + 1):
		rnd_cnt = random.choice(db)
		print(f'Question {rnd_cnt["question"]}\n'
			  f'[ ] {rnd_cnt["answer1"]}\n'
			  f'[ ] {rnd_cnt["answer2"]}\n')
		usr_answer = str(input('Your answer:\t'))
		if usr_answer == rnd_cnt["correct_answer"]:
			print('Correct!')
		else:
			print(f'Incorrect answer - {rnd_cnt["correct_answer"]}')


def main():
	# csv_writer(get_content(get_urs(url)), 'db_out.csv')
	game_loop()


if __name__ == '__main__':
	main()
