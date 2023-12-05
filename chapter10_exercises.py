from pathlib import Path
'''#10.1, #10.2

path = Path('learning_python.txt')

contents = path.read_text()

print(contents)

lines = contents.splitlines()

for line in lines:
	line.replace('Python', 'C')
	print(line.replace('Python', 'C'))

message = 'dogs'
print(message.replace('dogs', 'cats'))

#10.3

path = Path('guest_book.txt')
print('Press q to exit anytime')

while True:
	all_guest_names = path.read_text()
	guest_name = input('Please enter your name: ')
	if guest_name == 'q':
		break
	all_guest_names += guest_name + '\n'
	path.write_text(all_guest_names)

contents = path.read_text()
print(contents)

#10.4, 10.5

print('Press q to exit')

with open('responses.txt', 'a') as f:
	while True:
		response = input("Please tell us why you like programming ")
		if response == 'q':
			break
		f.write(response + '\n')

#10.6, 10.7

while True:
	a = input('Enter first number ')
	b = input('Enter second number ')

	try:
		c = int(a) + int(b)
	except ValueError:
		print("you can enter only numbers")
	else:
		print("The result is ", c)
		break

#10.8, #10.9, #10.10

path = Path('dogs.txt')

contents = path.read_text()

lines = contents.splitlines()

print(contents.count('the '))

#10.11, 10.12
try: 
	filename = Path('favorite_number2.txt')
	filename.write_text("10	")
except FileNotFoundError:
	print('The file does not exists')
else:
	favourite_number = filename.read_text()
	print(f'We know that your favourite number is ' + favourite_number)'''

#10.13
filename = Path('user.txt')
user_name = filename.write_text('Aditi')

if user_name != 'Juhi':
	user_name = 'Juhi'

filename.write_text(user_name)









