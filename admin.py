from users_module import User

class Admin(User):

	def __init__(self, first, last, age, location):
		super().__init__(first, last, age, location)
		self.privilege = Privileges()


class Privileges:
	def __init__(self):
		self.privileges = ["Add", "Delete", "Update", "Read"]

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)