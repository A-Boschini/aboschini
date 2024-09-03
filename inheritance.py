# Parent Class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the Vehicle Class!")

# Chiled Class
class Car(Vehicle):
    def Car_data(self):
        print("Hello from the Car Class!")

# Motor Class
class Motor(Vehicle):
    def Motor_data(self):
        print("Hello from the Motor Class!")

#Bike Child Class
class Bike(Vehicle):
    def Bike_data(self):
        print("Hello from the Bike")

# Object based on Car
car01 = Car()
car02 = Motor()
bike01 = Bike()

bike01.Vehicle_data()
bike01.Bike_data()
print("********************")
# Get Vehicle data
car01.Vehicle_data()
car01.Car_data()
car02.Motor_data()