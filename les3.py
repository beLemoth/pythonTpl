# exceptions

# --------------------------------------------

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

# simple_list = [1, 8, 10, 12, 5, 65, 78];
# last_index = len(simple_list) - 1;

# try:
# 	user_index = int(input('write index of element: '));

# 	if user_index > last_index :
# 		raise IndexError('too much');
# 	elif user_index < 0 :
# 		raise IndexError('index must be more than zero');

# except IndexError as e :
# 	print(e);
# except ValueError:
# 	print('wrong number');	

# else :
# 		print(simple_list[user_index]);	

# ---------------------------------------------

# functions

# ---------------------------------------------

# def some_function(first_value, second_value):
# 	if first_value > 0 and second_value > 0 :
# 		return first_value + second_value;
# 	elif first_value < 0 and second_value < 0 :
# 		return first_value - second_value;

# 	return 0;

# print(some_function(-2,-3));

# ----------------------------------------------

# def max_value(val1, val2, val3):

# 	if val1 > val2 :
# 		if val3 > val2 :
# 			print('{} {}'.format(val1, val3));
# 		else :
# 			print('{} {}'.format(val1, val2));
# 	elif val3 > val1 :
# 		print('{} {}'.format(val2, val3));


# max_value(5,2,3);		

# ----------------------------------------------

# def update_list(input_list, flag):
# 	out_list_odd = [];
# 	out_list_even = [];

# 	for item in input_list :
# 		if bool(item%2) :
# 			out_list_even.append(item);
# 		else :
# 			out_list_odd.append(item);	

# 	return out_list_odd if flag else out_list_even;

# print(update_list([1,2,3,4,5,6], False));	

# ----------------------------------------------

# arguments types 

# ----------------------------------------------

# def max_min (*args) :
# 	max_value = min_value = args[0];

# 	for value in args :
# 		if value > max_value :
# 			max_value = value;
# 		if value < min_value :
# 			min_value = value;

# 	return (min_value, max_value);			

# print(max_min(1,2,10,56,-2,45));	

# ----------------------------------------------

# def string_case(string, case = True):
# 	if case :
# 		return string.lower();
	
# 	return string.upper();

# print(string_case('HobjJjjsj', False));

# ----------------------------------------------

def strings_concat(*args, glue=':'):
	out_string = '';
	idx = 0;
	for item in args :
		if len(item) > 2 :
			out_string += (glue + item) if idx else item;
			idx += 1;
		
	return out_string;	

print(strings_concat('as', 'adsadsdad', 'asdasdsda')); 

