questions = {
	'Какой язык я изучаю':'python',
	'Как называется тип данных представляющий собой неизменяемый список':'tuple',
	'Как называется тип данных представляющий собой изменяемый список':'list',
	'Функция определения типа данных':'type',
	'Тип данных строка':'str'
				};

rightAnswer = 0;

for question in questions:
	answer = input('{}?: '.format(question));
	if answer.lower() == questions[question]:
		rightAnswer += 1;

print('Дано ответов {}, из них верно {}'.format(len(questions), rightAnswer));	