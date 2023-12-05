from city_functions11 import get_formated_string
#11.1, 11.2
def test_city_country():
    formated_city = get_formated_string('Mumbai', 'India')
    assert formated_city == 'Mumbai, India'