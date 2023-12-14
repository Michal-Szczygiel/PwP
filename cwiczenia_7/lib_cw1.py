class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return "{} {}, age: {}".format(self.name, self.surname, self.age)
    

class Student(Person):
    def __init__(self, name, surname, age, index_number):
        Person.__init__(self, name, surname, age)
        self.index_number = index_number
