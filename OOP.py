# Define a base class for ElectronicDevice
class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand  # Brand of the device
        self.model = model  # Model of the device

    def power_on(self):
        return f"{self.brand} {self.model} is now powered on."

    def power_off(self):
        return f"{self.brand} {self.model} is now powered off."


# Define a derived class for Smartphone that inherits from ElectronicDevice
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # Initialize attributes from the parent class
        self.storage = storage  # Storage capacity in GB
        self.camera_megapixels = camera_megapixels  # Camera resolution in megapixels

    def take_photo(self):
        return f"{self.brand} {self.model} took a photo with its {self.camera_megapixels}MP camera."

    def install_app(self, app_name):
        return f"{app_name} has been installed on {self.brand} {self.model}."

    def __str__(self):
        return f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, Camera: {self.camera_megapixels}MP"


# Define another derived class for Smartwatch to explore polymorphism
class Smartwatch(ElectronicDevice):
    def __init__(self, brand, model, battery_life):
        super().__init__(brand, model)  # Initialize attributes from the parent class
        self.battery_life = battery_life  # Battery life in hours

    def track_steps(self, steps):
        return f"{self.brand} {self.model} tracked {steps} steps."

    def __str__(self):
        return f"Smartwatch: {self.brand} {self.model}, Battery Life: {self.battery_life} hours"


# Example usage
if __name__ == "__main__":
    # Create a Smartphone object
    phone = Smartphone("Apple", "iPhone 14", 128, 12)
    print(phone)
    print(phone.power_on())
    print(phone.take_photo())
    print(phone.install_app("Instagram"))
    print(phone.power_off())

    # Create a Smartwatch object
    watch = Smartwatch("Samsung", "Galaxy Watch 5", 48)
    print(watch)
    print(watch.power_on())
    print(watch.track_steps(5000))
    print(watch.power_off())