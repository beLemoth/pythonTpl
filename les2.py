# simpleLIst = [8, 10, 16, 25, 2, 10, 6, 78, 120, 4];
# simpleLIst.sort();
# print(simpleLIst);

# -------------------------------------------------------

# dictionary = {8: '8', 10: '10', 2:'2', 11:'11', 45:'45'};
# for item in dictionary:
# 	print('{}:{}'.format(item, dictionary[item]));

# -------------------------------------------------------

# simpleTuple = (2.53, 0.68, 23.54, 33.44, 2.85, 7.85, 9.55, 1.23, 5.66, 100.45);
# minValue = maxValue = simpleTuple[0];

# for currentValue in simpleTuple:
# 	if currentValue < minValue :
# 		minValue = currentValue;
# 	elif currentValue > maxValue:
# 		maxValue = currentValue;

# print(minValue, maxValue);		

# --------------------------------------------------------

# textList = ['Earth', 'Russia', 'Moscow'];

# outputStr = '';
# index = 0;

# for word in textList:
# 	outputStr += ( ' -> ' if bool(index) else '') + word;
# 	index += 1;

# print(outputStr);	

# ---------------------------------------------------------

# string = '/bin:/usr/bin:/usr/local/bin';
# print(string.split(':'));

# ---------------------------------------------------------

# for number in range(1, 101):
# 	print('{} - '.format(number) + ('не ' if bool(number%7) else '') + 'делится');

# ---------------------------------------------------------

# simpleList = ['Earth', 'Russia', 'Moscow'];
# index = 0;

# for item in simpleList:
# 	print('{} - {}'.format(item, index));
# 	index += 1;

# ---------------------------------------------------------

# simpleList = ['Earth', 'to-delete', 'Russia', 'to-delete', 'Moscow', 'to-delete'];

# for item in simpleList:
# 	if item == 'to-delete':
# 		simpleList.remove(item);	

# print(simpleList);		

# ---------------------------------------------------------

currentValue = 10;
stopValue = 1;

while currentValue >= stopValue :
	print(currentValue);
	currentValue -= 1;

