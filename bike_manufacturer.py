from bicycle import Bicycle

class Manufacturer(object):
    """docstring for Manufacturer"""
    # Procedure to manufacture bicycles
    def make_bike(self,number,manufacturer,margin):
        bicycles = {}
        for number in range(number):
            while True:
                bike = Bicycle(manufacturer)
                if bike.model_name not in bicycles.keys():
                    bicycles[bike.model_name] = bike
                    # Add the margin of the bike manufacturer to the cost of the bike
                    bicycles[bike.model_name].cost *= 1 + margin
                    break
                else:
                    print("The chosen model already exists, let's try again")
                    continue
        return bicycles
    
    def __init__(self, manufacturer_name,margin):
        self.manufacturer_name = manufacturer_name
        self.margin = margin
        self.inventory = self.make_bike(3,self.manufacturer_name,self.margin)
        for bike in self.inventory:
            print self.inventory[bike]
            print ""
    def __str__(self):
        return "{}".format(self.manufacturer_name)