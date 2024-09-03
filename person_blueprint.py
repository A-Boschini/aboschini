class Person:
    """Person main class"""
    def __init__(self, name, age, personID):
        self.name = name
        self.age = age
        self.personID = personID

    def display_data(self):
        print("Hi, my name is ",self.name,",my age is", self.age, ",and my personal ID is", self.personID)

person01 = Person("Alberto", 58, 123)
person02 = Person("Gino", 61, 13)
person03 = Person("Fiona", 18, 5)

person01.display_data()
person02.display_data()
person03.display_data()

#print(person01.name)
#print(person01.age)
#print(person01.personID)

#print(person02.name)
#print(person02.age)
#print(person02.personID)

#print(person03.name)
#print(person03.age)
#print(person03.personID)