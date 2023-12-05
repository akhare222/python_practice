#11.1, 11.2
def get_formated_string(city, country, population = ''):
    if population:
        formated_str = f'{city}, {country} - population {population}'
    else:
        formated_str = f'{city}, {country}'
    return formated_str

