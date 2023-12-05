#9.1, 9.2, 9.4, 9.6
class Restaurant:
	"""Class to create a simple restaurant"""

	def __init__(self, restaurant_name, cuisine_type='Indian'):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 10

	def describe_restaurant(self):
		desctiption = f'The {self.restaurant_name} serves {self.cuisine_type} food\n'

		print(desctiption)

	def open_restaurant(self):
		print("The restaurant is now open")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment_by):
		self.number_served += increment_by


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type='ice creams'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["chocolate", "strawberry"]

	def show_flavors(self):
		for flavor in self.flavors:
			print(flavor)


