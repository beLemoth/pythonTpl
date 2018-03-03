# exceptions

# user_answer = int(input('write number: '));

# try:
# 	if (user_answer+1)%2:
# 		raise ValueError('четное число');
# 	if user_answer < 0:
# 		raise TypeError('меньше ноля');
# 	elif user_answer > 10:
# 		raise IndexError('больше 10');

# except ValueError as e:
# 	print(e);		

# except TypeError as e:
# 	print(e);	

# except IndexError as e:
# 	print(e);

# ---------------------------------------------

simple_list = [1, 8, 10, 12, 5, 65, 78];
last_index = len(simple_list) - 1;

try:
	user_index = int(input('write index of element: '));

	if user_index > last_index :
		raise IndexError('too much');
	elif user_index < 0 :
		raise IndexError('index must be more than zero');
	else :
		print(simple_list[user_index]);

except IndexError as e :
	print(e);
except ValueError:
	print('wrong number');	


