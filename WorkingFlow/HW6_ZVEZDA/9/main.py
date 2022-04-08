from bs4 import BeautifulSoup
from requests import get
import csv
from random import randint

url = r'https://www.usingenglish.com/quizzes/29.html'
HEADERS = {
		'accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36'
}


def get_urs(url, params=''):
	r = get(url, headers=HEADERS, params=params)
	return r


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
								'strong').get_text(
								strip=True),
						'answer2':        item.find('label', attrs={'for': f'question{count}1'}).find(
								'strong').get_text(
								strip=True),
						'correct_answer': 'correct answer here',
				}
		)
		count += 1
	print(f'>> DataBase Status: Created and Stored - {count-1} elements in DB')

	return questions


def csv_writer(data: list, filename: str):
	with open(filename, 'w') as f:
		writer = csv.DictWriter(
				f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
		writer.writeheader()
		for d in data:
			writer.writerow(d)
	print(f'>> DataBase Status: Re-Wrote as CSV file with name {filename}')


def game_loop():


# db = csv.reader(open('db_out.csv'))
# question_cnt = int(input('Enter amount of questions in game:\t'))
# for counter in range(question_cnt+1):
# 	for row in db:
# 		# print(f'Question {row[0]}. {row[1]}.\n'
# 		# 	  f'[ ] {row[2]}\n'
# 		# 	  f'[ ] {row[3]}\n')
# 		# usr_answer = input('Your answer:\t')
# 		print(row)
# with open('db_out.csv') as f:
# 	reader = csv.reader(f)
# 	for row in reader:
# 		print(row)
	pass

def main():
	csv_writer(get_content(get_urs(url).text), 'db_out.csv')


# game_loop()


if __name__ == '__main__':
	main()
