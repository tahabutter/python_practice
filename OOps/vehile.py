# Inheritance Problem

class Vehicle:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def display_info(self):

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Car(Vehicle):

    def __init__(self, brand, model, seats):

        super().__init__(brand, model)

        self.seats = seats

    def display_car_info(self):

        self.display_info()

        print(f"Seats: {self.seats}")

class Bike(Vehicle):

    def __init__(self, brand, model, type):

        super().__init__(brand, model)

        self.type = type

    def display_bike_info(self):

        self.display_info()

        print(f"Type: {self.type}")


v2 = Car("Honda", "Civic", 5)

v2.display_car_info()

b1 = Bike("Yamaha", "R15", 155)

b1.display_bike_info()