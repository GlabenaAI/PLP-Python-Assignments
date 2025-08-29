# Assignment 1: Creating my own Smartphone Class
# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def call(self, number):
        return f"{self.model} is calling {number}..."

    def browse(self, website):
        return f"Browsing {website} on {self.model}."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}mAh)"


# Inherited class
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    # Polymorphism: override browse method
    def browse(self, website):
        return f"{self.model} (Pro) loads {website} super fast with 5G!"

    # New method unique to Pro
    def take_photo(self):
        return f"Taking a {self.camera_megapixels}MP photo with {self.model}!"

    def __str__(self):
        return f"{self.brand} {self.model} Pro ({self.storage}GB, {self.battery}mAh, {self.camera_megapixels}MP Camera)"


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone2 = SmartphonePro("Apple", "iPhone 15", 256, 4300, 48)

print(phone1)
print(phone1.call("123-456-7890"))
print(phone1.browse("www.openai.com"))

print("\n---\n")

print(phone2)
print(phone2.call("987-654-3210"))
print(phone2.browse("www.github.com"))
print(phone2.take_photo())

# Activity 2: Polymorphism Challenge
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


# Child classes with different move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")


# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()