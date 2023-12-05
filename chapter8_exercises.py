#8.1
def display_message():
	print('This chapter is teaching how to use functions\n')

display_message()

#8.2
def print_favourite_book(title):
	print(f'One of my all time favourite books is "{title}"\n')

print_favourite_book('The monk who drove a ferrari')

#8.3, 8.4
def make_shirt(size="Large", message="I Love Python"):
	print(f'The size of the shirt that needs to be made is "{size}"')
	print(f'The message that needs to be printed on the shirt is "{message}"\n')

make_shirt('XL','This is the best day ever')
make_shirt(message='To be or not to be')
make_shirt("Small", message="I love java too")

#8.5, 8.6
def describe_city(city, country="India"):
	print(f'"{city}, {country}"')

describe_city('Mumbai')
describe_city(city = 'Kolkota')
describe_city(city = 'NYC', country = 'USA')

#8.7
def make_album(artist_name, album_title, number_of_songs = None):
	album_info = {}
	album_info['name'] = artist_name
	album_info['title'] = album_title
	if number_of_songs:
		album_info['number of sogns'] = number_of_songs

	return album_info

print(make_album('Lata Mangeshkar', 'Golden times', 8))
print(make_album('Asha bhosle', 'New times'))

#8.8
def make_album_with_user():
	album_info = {}
	name = input('Enter name of the artist. "q" to quit')
	if name is not "q":
		album_info["name"] = name
	else:
		return "The user entered q"

	album = input('Enter name of the album. "q" to quit')
	if album is not "q":
		album_info["album"] = album
	else:
		return "The user entered q"

	return album_info

print(make_album_with_user())

#8.9, #8.10, 8.11
message_1 = "This is message 1"
message_2 = "this is message 2"
message_3 = "This is message 3"

messages = [message_1, message_2, message_3]
sent_messages = []

def show_messages(messages):
	while messages:
		message = messages.pop(0)
		print(message)
		sent_messages.append(message)

show_messages(messages[:])
print("Inside messages", messages)
print("Inside sent messages", sent_messages)


#8.12
def make_sandwich(*toppings):
	for topping in toppings:
		print(f'Adding {topping}')
	print()

make_sandwich('cheese','tomato')
make_sandwich('potato','paneer','mozarella')

#8.13
def build_profile(first, last, **user_profile):
	user_profile['first_name'] = first
	user_profile['last_name'] = last

	return user_profile

user = build_profile("Aditi", "Khare", gender="Female", location="NYC", hobbies="chess, tennis, coding")
print(user)

#8.14

def make_car(manufacturer, model_name, **car):
	car["manufacturer"] = manufacturer
	car["model_name"] = model_name

	return car

car = make_car("Fiat", "Chrysler 1999", color = "blue", optional_feature="Leather seat")
print(car)

#8.15, 8.16
from printing_models import *

designs = ['mini robot', 'keys', 'tv']
completed_models = []

print_models(designs, completed_models)
show_models(completed_models)