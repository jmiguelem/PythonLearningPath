class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 40000)

print(emp_1)
print(emp_2)
print(" ")
"""
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Shafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 40000

"""

print(emp_1.email)
print(emp_2.email)
print(" ")

print(emp_1.fullname())
print(Employee.fullname(emp_2))
print(" ")

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(" ")

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(" ")

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
emp_1.raise_amount = 1.04
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(" ")

print(Employee.num_of_emps)
emp_3 = Employee('Name', 'Surname', 'Wage')
print(Employee.num_of_emps)



