#4.1 -> for loop for list of pizzas
pizzas = ['cheese pizza', 'jalepeno pizza', 'vegetable pizza', 'marinara pizza', 'thin crust pizza']

for pizza in pizzas:
	print(f'I like {pizza}')

print("I really love pizzas!")

#4.2
animals = ['dog', 'cat', 'rabbit']

for animal in animals:
	print(f'I would really like {animal} as a pet')

print('Any of the above animals would make a great pet')

#4.3 print inclusive numbers from 1 to 20
for number in range(1, 21):
	print(number, end = ' ')
print()

#4.4 print inclusive numbers from 1 to 1 million
'''for number in range(1,1_000_001):
	print(number, end=' ')
print()'''

#4.5 print min, max and sum for numbers 1 to 1 million
numbers = [x for x in range(1, 1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6 print odd numbers from 1 to 20
for odd_number in range(1, 21, 2):
	print(odd_number, end = ' ')
print()

#4.7 multiples of 3 from 3 to 30
for i in range(1, 11):
	print(3 * i, end = ' ')
print()

#4.8, 4.9 print cubes from 1 to 10 using list comprehension
cubes = [x**3 for x in range(1, 11)]
for cube in cubes:
	print(cube, end = ' ')
print()

#4.10 print first 3 items
print('The first 3 pizzas are: ')
for pizza in pizzas[:3]:
	print('\t' + pizza)
print()

#4.11 Friends pizza using your pizza as a copy
friends_pizzas = pizzas[:]
pizzas.append('extra cheese pizza')
friends_pizzas.append('thick crust pizza')
print('my pizzas are: ', pizzas)
print('my friends pizzas are', friends_pizzas)

#4.12 use for loops to print food
for pizza in friends_pizzas:
	print(pizza, end = ' ')
print()

#4.13 use tuples to store 5 foods for a buffet style restaurant
food_items = ('rice', 'daal', 'potato curry', 'chapati', 'papad')
print('The food items offered in our buffet style restaurant are: ')
for food_item in food_items:
	print('\t' + food_item)

food_items = ('rice', 'daal', 'peas curry', 'naan', 'papad')
print('The food items offered in our buffet style restaurant are: ')
for food_item in food_items:
	print('\t' + food_item)






