class Person:
    """Person main class"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

person01 = Person("Alberto", 58, 123)
person02 = Person("Gino", 61, 13)
person03 = Person("Fiona", 18, 5)

print(person01.name)
print(person01.age)
print(person01.personID)

print(person02.name)
print(person02.age)
print(person02.personID)

print(person03.name)
print(person03.age)
print(person03.personID)