# # person class

# ----------------------------------------

# class Person(object):
# 	def __init__(self, name, age):
# 		self.name = name;
# 		self.age = age;
# 		self.known = [];


# 	def know(self, person):
# 		self.known.append(person);

# 	def is_known(self, person):
# 		print('known' if bool(self.known.count(person)) else 'unknown');	


# person1 = Person('alex', 19);

# person2 = Person('alice', 20);

# person3 = Person('mike', 30);

# person1.know(person2);

# person1.is_known(person2);

# person1.is_known(person3);

# person1.know(person3);

# person1.is_known(person3);
# person2.is_known(person3);

# ----------------------------------

# printer class

# ----------------------------------

# class Printer(object):
# 	def __init__(self):
# 		values_list = [];

# 	def log(self, *values):
# 		values_list = [item for item in values];
# 		print(' '.join(values_list));


# class FormatedPrinter(Printer):
# 	def form_log(self, *values):
# 		print('*********************');
# 		self.log(*values);			
# 		print('*********************');


# form = FormatedPrinter();
# form.form_log('2','3','4');		

# -----------------------------------------

# animals and humans

# -----------------------------------------

class Animal(object):
	
	def __init__(self, aggression = False):
		self.aggression = aggression;

class Human(object):

	def is_dangerous(self, animal):
		print('dangerous' if animal.aggression else 'not dangerous');		


tiger = Animal(True);
horse = Animal(False);

john = Human();

john.is_dangerous(tiger);
john.is_dangerous(horse);