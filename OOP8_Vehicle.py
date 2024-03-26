class Vehicle:
    
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  # In Km/h
        self.fuel_type = fuel_type

# Write your code below:

class Car(Vehicle):
    def __init__(self, color, speed, fuel_type, num_doors, is_electric):
        Vehicle.__init__(color, speed, fuel_type)
        self.num_doors = num_doors
        self.is_electric = is_electric

my_car = Car('black', 105, 'unleaded gas', 4, False)
print("Here is the info about my car")
print(f"Color: {my_car.color}")
print(f"Speed: {my_car.speed}")
print(f"Fuel Type: {my_car.fuel_type}")
print(f"Number of Doors: {my_car.num_doors}")
if my_car.is_electric == True:
    print(f"Is Electric: yes")
else:
    print("Is electric: No")