#6.1
person_1 = {
	'first_name' : 'Aditi',
	'last_name' : 'Khare',
	'location' : 'Jersey City'
}

for key, value in person_1.items():
	print(f'\nThe key is {key} and the value is {value}')

#6.2 6.9
favourite_numbers = {
	'Jen' : [5, 8],
	'Ken' : [10, 20, 30],
	'Mary' : [12],
	'James' : [15],
	'Jason' : [13]
}

for name, favourite_number in favourite_numbers.items():
	if len(favourite_number) == 1:
		print(f"\n{name}'s favourite number is {favourite_number[0]}")
	else:
		print(f"\n{name}'s favourite number are")
		for number in favourite_number:
			print('\t' , number)

#6.3, 6.4
glossary = {
	'for' : 'used to loop a collection like a list, dictionary etc',
	'True' : 'A keyword which signifies that an expression or value will be evaluated to a true value',
	'False' : 'A keyword which signifies that an expression or value will be evaluated to a false value',
	'while' : 'Another way to loop usually when the number of iterations is not known in advance',
	'list' : 'A collection where usually similar objects are stored in an array'
	}

for keyword, definition in glossary.items():
	print(f'\n{keyword}:')
	print(f'\t{definition}')

#6.5
rivers_and_countries = {
	'nile' : 'egypt',
	'Ganges' : 'India',
	'Brahmaputra' : 'Pakistan',
	'Hudson' : 'USA',
	'Saraswati' : 'India'
	}

for river, country in rivers_and_countries.items():
	print(f'\n{river} flows through {country}')

for river in rivers_and_countries.keys():
	print(river)

for country in rivers_and_countries.values():
	print(country)

#6.6
favorite_languages = {'Jen' : 'Python', 'Mark' : 'Java', 'ken' : 'C++', 'sarah' : 'Python'}
friends = ['sarah', 'Angela', 'mike']

for friend in friends:
	if friend in favorite_languages.keys():
		print(f'Thanks for taking the poll {friend.title()}')
	else:
		print(f'Please take the poll {friend.title()}')

#6.7
person_1 = {
	'first_name' : 'Aditi',
	'last_name' : 'Khare',
	'location' : 'Jersey City'
	}	

person_2 = {
	'first_name' : 'Mike',
	'last_name' : 'Harrison',
	'location' : 'New York City'
	}	

person_3 = {
	'first_name' : 'Angela',
	'last_name' : 'Gray',
	'location' : 'LA'
	}

people = [person_1, person_2, person_3]

for person in people:
	print(f'{person["first_name"]} {person["last_name"]} lives in {person["location"]}')

#6.8
pet_1 = {'type' : 'cat',
'owner' : 'Jessica'
}

pet_2 = {'type' : 'dog',
'owner' : 'Mike'
}

pets = [pet_1, pet_2]

for pet in pets:
	print(f'This {pet["type"]} is owned by {pet["owner"]}')

#6.9
favourite_places = {
	"Mike" : ["New York", "London"],
	"Sarah" : ["Delhi"],
	"Jessica" : ["Moscow"]
}

for name, favourite_place in favourite_places.items():
	if(len(favourite_place) == 1):
		print(f"{name}'s favourite place is {favourite_place[0]}.")
	else:
		print(f"{name}'s favourite places are:")
		for place in favourite_place:
			print('\t', place)

#6.11
cities = {
	'NYC' : {
		'population' : 1_000,
		'fact' : 'One of the oldest cities in the US and also the financial capital'
	},
	'Mumbai' : {
		'population' : 2000,
		'fact' : 'Financial district of India'
	}
}

for city, info in cities.items():
	print(f'\nWe will discuss about {city}:')
	print(f'\tThe population here is {info["population"]}')
	print(f'\tThe fact of this city is {info["fact"]}')
