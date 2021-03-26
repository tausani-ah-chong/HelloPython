# My first function in Python!
def say_hi(name):
    if name == '':
        print("You haven't entered a name, please try again")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)


# name = input()
# say_hi(name.upper())


# creating class practice
class House:
    door_locked = True
    house_cleaned = False

    def walk_in(self):
        if self.door_locked:
            print("You need a key to unlock the door first")
        else:
            print("Alright lets get this party started")

    def use_key(self):
        self.door_locked = False
        print("Door unlocked!")

    def start_party(self):
        if self.house_cleaned:
            print("Turn the music up! 🥳🕺")
        else:
            print("Yo come on this place is a mess! Let's clean first")

    def clean(self):
        self.house_cleaned = True
        print("Alright looking good!")


# Class with constructor
class Car:
    def __init__(self, colour, make):
        self.colour = colour
        self.make = make


red_car = Car("red", "toyota")

# print(red_car.make)


# play with dictionaries
carpark = {
    "toyota": "red",
    "mercedes": "white",
    "bmw": "red",
}

carpark2 = {
    "mazda": "black",
    "mitsubishi": "orange",
    "holden": "blue",
}

carpark["bmw"] = "black"
del(carpark["toyota"])
makes = carpark.keys()

# print(carpark)
# print(carpark["bmw"])
# print(makes)

# merge dictionaries = {**carpark, **carpark2}
# in version 3.9 merging dictionaries is simpler
merged = carpark | carpark2
for make, colour in merged.items():
    print(make, ":", colour)
