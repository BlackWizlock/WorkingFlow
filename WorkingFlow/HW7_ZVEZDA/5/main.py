questions = [
		{
				'text':    'Вы приплыли с друзьями в бар и не знаете, что взять. Как поступите?',
				'options': {
						'A': 'Посмотрю, что берут другие.',
						'B': 'Выберу пару диковинных названий и загуглю, что это такое.',
						'C': 'Заставлю бармена рассказать мне про каждый пункт в меню!',
				}
		},
		{
				'text':    'Придя на работу, вы узнали, что у вас теперь новое \n'
						   'руководство и приоритеты отдела меняются, но это не точно. \n'
						   'Надо разобраться, что к чему и какие теперь правила. Как поступите?',
				'options': {
						'A': 'Отправлюсь в курилку послушать сплетни.',
						'B': 'Буду ждать объявления или планерки.',
						'C': 'Просто зайду к новому руководителю и спрошу, как дела.',
				}
		},
		{

				'text':    'Вы находитесь дома и ждете крупную доставку дорогой посылки, \n'
						   'но узнаете, что она задерживается. Вам нужно отправиться на работу, \n'
						   'но и доставки нужно дождаться. Как поступите?',
				'options': {
						'A': 'Попрошу подменить меня соседей, родственников или друзей.',
						'B': 'Отменю доставку, что ж, бывает и такое.',
						'C': 'Позвоню в службу доставки и поставлю всех на уши!',
				}
		},
]

result = {
		'A':         'Вы — стайная селедка.',
		'B':         'Вы — задумчивая камбала.',
		'C':         'Вы — активная щука.',
		'Непонятно': 'Мы не смогли определить, кто вы. Будете лещом!',
}

usr_answer = {
		'A': 0,
		'B': 0,
		'C': 0,
}


def main():
	print('Тест на рыбий характер!\nДайте ответ на вопросы:')
	for item in questions:
		print(item['text'])
		for answer, textpart in item['options'].items():
			print(f'{answer}. {textpart}')
		while True:
			usr_ans = str(input('Ваш ответ:\t')).upper()
			if usr_ans in ('A', 'B', 'C'):
				usr_answer[usr_ans] += 1
				break
			else:
				print('Доступные варианты A, B, C!')
	if usr_answer['A'] == usr_answer['B'] == usr_answer['C']:
		print(result['Непонятно'])
	else:
		print(result[max(usr_answer, key=usr_answer.get)])


if __name__ == '__main__':
	main()
