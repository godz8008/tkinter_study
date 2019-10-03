class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def empInfo(self):
        print('{} {}'.format(self.name, self.salary))

emp1 = Employee('김말똥',2000)
emp2 = Employee('고길동',3000)

emp1.empInfo()
emp2.empInfo()