class Vehicle:
    def vehicle(self):
        print("A")

class Train(Vehicle):
    def train(self):
        print("B")

class Car(Vehicle):
    def car(self):
        print("C")

class BMW(Car,Vehicle):
    def bmw(self):
        print("C")

ob = BMW()
ob.vehicle()
ob.car()
ob.bmw()