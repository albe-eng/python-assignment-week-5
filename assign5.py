# Parent class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # private attribute for encapsulation
    
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")
        self.__battery -= 5   # reduce battery after each call

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} is now fully charged.")

    def get_battery(self):
        return f"Battery level: {self.__battery}%"
    # Child class inheriting from Smartphone
class Smartwatch(Smartphone):
    def show_time(self):
        print("Showing time on the smartwatch screen.")

# Creating objects
phone1 = Smartphone("Samsung", "S23", 80)
watch1 = Smartwatch("Apple", "Watch Series 9", 50)

# Using methods
phone1.make_call("072456789")
print(phone1.get_battery())
watch1.show_time()




class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()


