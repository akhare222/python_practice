#5.1
car = 'Subaru'
print('Is car Subaru? I predict yes')
print(car.lower() == 'subaru')

print('\nIs car Audi? I predict no')
print(car.lower() == 'Audi')

#5.2
age = 18
country = 'India'

if age < 18 or country == 'India':
	print('You are too young to drive')
else:
	print('You are old enough to drive')

pizzas = ['Thin crust', 'Thick crust', 'Extra cheese', 'Marinara']

requested_pizza = 'Thin crust'

if requested_pizza in pizzas:
	print(f'{requested_pizza} is there')
else:
	print(f'{requested_pizza} is not there')

#5.3, 5.4, 5.5
alien_color = 'green'

if alien_color == 'green':
	print('You earned 5 points')
elif alien_color == 'yellow':
	print('You earned 10 points')
elif alien_color == 'red':
	print('You earned 15 points')

#5.6
age = 38
stage = ''

if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'kid'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
elif age >= 65:
	stage = 'elder'
print(f'You are a {stage}')

#5.7
favourite_fruits = ['Mangoes', 'oranges', 'bananas']

if 'bananas' in favourite_fruits:
	print('You really like bananas')
if 'kiwi' in favourite_fruits:
	print('You really like kiwi')
if 'Mangoes' in favourite_fruits:
	print('You really like Mangoes')
if 'strawberries' in favourite_fruits:
	print('You really like strawberries')
if 'oranges' in favourite_fruits:
	print('You really like oranges')

#5.8, 5.9

user_names = ['Jordan', 'Peter', 'Mike', 'Angela', 'admin']

if user_names:
	for user in user_names:
		if user == 'admin':
			print(f'Hello {user}, would you like to see status report?')
		else:
			print(f'Hello {user}, thank you for login in again')
else:
	print('There are no users in the system')

#5.10
current_users = ['Jordan', 'Peter', 'Mike', 'Angela', 'admin']
new_users = ['Michael', 'Aditi', 'Peter', 'Angela', 'Sam']

for user in new_users:
	if user in current_users:
		print(f'You need to choose a new username {user}')
	else:
		print(f'{user} is available')

#5.11
ordinals = ['first', 'second', 'third', 'fourth']

for ordinal in ordinals:
	if 'th' in ordinal:
		print('Number greater than or equal to 3')
	else:
		print('Number less than 3')


 




