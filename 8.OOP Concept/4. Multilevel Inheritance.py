class Vehicle:
    def vehicle(self):
        print("A")

class Car(Vehicle):
    def car(self):
        print("b")

class BMW(Car):
    def bmw(self):
        print("B")

# Create an instance of the BMW class
ob = BMW()

# Call the methods using the instance
ob.vehicle()
ob.car()
ob.bmw()
