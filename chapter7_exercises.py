#7.1
print('\nEntering 7.1')
wanted_car = input("What kind of rental car would you like? ")
print(f'Let me see if we can find a {wanted_car} for you')

#7.2
print('\nEntering 7.2')
number_of_guests = input("How many guests are there in your group? ")


if int(number_of_guests) > 8:
	print('\nYou will have to wait')
else:
	print('\nYour table is ready')

#7.3
print('\nEntering 7.3')
number = int(input('Enter a number: '))

if number % 10 == 0:
	print('\nYou have entered a number divisible by 10')
else:
	print('\nThe number is not divisible by 10')

#7.4, 7.6
print('\nEntering 7.4')
print('press "quit" to exit')
active = True
prompt = 'What topping would you like? '
while active:
	topping = input(prompt)

	if topping != 'quit':
		print(f'We will add {topping} to your pizza')
	else:
		break

#7.5
print('\nEntering 7.5')
age = input('What is your age? ')
age = int(age)
if age < 3:
	print('Ticket is free')
elif age < 12:
	print('Ticket is $10')
else:
	print('Ticket is $15')

#7.7
while True:
	print("something")

#7.8, 7.9
print('\nEntering 7.8, 7.9')
sandwich_orders = ['tuna sandwich', 'pastrami','cheese grilled sandwich','pastrami', 'chicken sandwich','pastrami', 'tomato sandwich']
finished_orders = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich != 'pastrami':		
		print(f'I made you a {sandwich}')
		finished_orders.append(sandwich)
	else:
		print('We have run out of pastrami')

print('completed orders are ', finished_orders)

#7.10
print('\nEntering 7.10')
responses = {}
prompt_name = 'What is your name? '
prompt_response = 'Which is your dream destination? '
prompt_quit = 'Is another user going to take this poll? (yes/no)'
active = True

while active:
	name = input(prompt_name)
	response = input(prompt_response)

	responses[name] = response
	quit_message = input(prompt_quit)

	if quit_message == 'no':
		active = False

for name, response in responses.items():
	print(f"{name}'s favourite destination is {response} \n")



