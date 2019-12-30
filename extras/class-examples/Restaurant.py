class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name + " serves " + \
                self.cuisine_type + " cuisine.")
    def open_restaurant(self):
        print("The new restaurant, " + self.restaurant_name + " is now open!")
    def increment_number_served(self, x):
        self.number_served += x

noodles = Restaurant("Noodles", "Asian")

print(noodles.restaurant_name)
print(noodles.cuisine_type)
noodles.describe_restaurant()
noodles.open_restaurant()