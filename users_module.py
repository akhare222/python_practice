#9.3, 9.5, 9.7, 9.8

class User:

	def __init__(self, first, last, age, location):
		self.first_name = first
		self.last_name = last
		self.age = age
		self.location = location
		self.login_attempts = 0
		

	def describe_user(self):
		user_description = f'{self.first_name} {self.last_name} lives in {self.location} and is {self.age} years old'
		print(user_description)

	def greet_user(self):
		print(f"Good morning {self.first_name} {self.last_name}\n")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

