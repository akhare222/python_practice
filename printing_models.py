def print_models(designs, completed_models):
	while designs:
		design = designs.pop(0)
		print(f'{design} is being printed')
		completed_models.append(design)
		

def show_models(completed_models):
	print(f'The completed models are: {completed_models}')