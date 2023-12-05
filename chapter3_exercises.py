names = ['Aditi', 'Ajeeta', 'Shayu']

for name in names:
	print(f"I would like to invite you to dinner {name}!")

print(f"{names[2]} won't be able to make in :( ")

names[2] = 'papa'

print(f"I am inviting {names[2]} instead ")

print("So all the invitees are: ")

for name in names:
	print(name, end = ' ')

print()

names.insert(0, 'mummy')
names.insert(1, 'yashi')
names.insert(2, 'arpit')
names.insert(0, 'rahul')
names.insert(int(len(names) / 2), 'maya')
names.append('arpita')
names.insert(20, 'rohit')
names.insert(20, 'shayu')

print("the new names list is: ", names)

for name in names:
	print(f"I invite you to my bday party {name}")


print("The number of people invited to dinner is " + str(len(names)))


