# Define a base class for Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name  # Name of the vehicle

    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")  # Enforce implementation in subclasses


# Define a derived class for Car
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road. 🚗"


# Define a derived class for Plane
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky. ✈️"


# Define a derived class for Boat
class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on the water. 🚤"


# Example usage
if __name__ == "__main__":
    # Create objects for each vehicle type
    car = Car("Sedan")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")

    # Demonstrate polymorphism
    vehicles = [car, plane, boat]  # List of vehicles
    for vehicle in vehicles:
        print(vehicle.move())  # Call the move() method for each vehicle