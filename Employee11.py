class Employee:

    def __init__(self, first, last, annual_salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary

    def give_raise(self, inc=5000):
        self.annual_salary += inc
        return self.annual_salary
