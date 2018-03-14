# numbers

# import random;

# def init_question():
# 	random.seed(version=2);
# 	return random.randrange(0, 100, 1);

# def check_the_answer(number):
# 	try:
# 		user_number = input('Input your number(1-100): ');
# 		user_number = int(user_number);
# 	except Exception:
# 		print('Not a number');
# 		return 0;	

# 	if user_number == number:
# 		print('Wonderfull!!!!');
# 		return 1;
# 	elif user_number < number:
# 		print('more');
# 	else:
# 		print('less');
# 	return 0;			
		

# def user_game(number):
# 	while not check_the_answer(number): 
# 		print('--------------');

# user_game(init_question());

# try:
# 	while input('Play again???:(Y/n) ').lower() == 'y':
# 		user_game(init_question());
# except Exception:
# 	print('Wrong answer');	

# print('Bye');

# gallows

import random
from random import choice
from string import ascii_uppercase

def get_word():
	return ''.join(choice(ascii_uppercase) for i in range(random.randrange(5, 12, 1)));

def user_answer_check(word):
	letter = input('Enter your letter: ');
	cached = ();
	try: 
		letter = letter.upper();
	except TypeError:
		print('wrong value');

	idx = 0;	
	for current_letter in word:
		if(current_letter == letter):
			cached += (idx,);
		idx += 1;			

	return cached;

def string_write(word, is_open):
	string = '';
	index = 0;
	for letter in word:
		if is_open[index]:
			string += letter;
		else:
			string += '_';
		index += 1;	

	print(string);		

def game_init():
	lives = 5;
	is_open = [];

	word = get_word();

	for letter in word:
		is_open.append(False);

	while lives > 0:
		print('{} lives left'.format(lives));
		string_write(word, is_open);
		answer = user_answer_check(word);

		if bool(answer):
			for index in answer:
				is_open[index] = True;
		else:
			lives -= 1;	

game_init();
		
while( input('You loose, wanna play again???:(Y/n) ').lower() == 'y'):
	game_init();		

print('Bye');
