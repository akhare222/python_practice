'''#9.10
from restaurant import Restaurant

rest = Restaurant("Taj", "Mixed")
rest.describe_restaurant()

#9.12
from admin import Admin

user_1 = Admin("Aditi", "Khare", 29, "Mumbai")

user_1.privilege.show_privileges()

#9.13
from random import randint

class Die:

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(randint(1, self.sides))


die = Die(20)
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()'''

#9.14
from random import choice

lottery_numbers = (10, 20, 30, 40, 99, 100, 'A', 'B', 'C', 'F')
winning_numbers = []
my_ticket = [100, 40, 'A', 'C']
i = 0
active = True

while(active):
	i += 1
	for i in range(4):
		winning_numbers.append(choice(lottery_numbers))

	while winning_numbers:
		num = winning_numbers.pop()
		if num not in my_ticket:
			break

	if not winning_numbers:
		print('the value of i is ', i)
		active = False
	else:
		winning_numbers = []


print(winning_numbers)








