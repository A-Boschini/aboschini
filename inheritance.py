# Parent Class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the Vehicle Class!")

# Chiled Class
class Car(Vehicle):
    def Car_data(self):
        print("Hello from the Car Class!")

# Object based on Car
car01 = Car()

# Get Vehicle data
car01.Vehicle_data()
car01.Car_data()