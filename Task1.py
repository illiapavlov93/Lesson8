class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        return 'Person: {}, {}, {}'.format(self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

c = Person('Bob', 'doctor', 4000)
print(c.__str__())
b = Manager('Paul', 5000)
print(b.__str__())