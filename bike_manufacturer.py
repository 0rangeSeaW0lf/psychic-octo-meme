from bicycle import Bicycle

class Manufacturer(object):
    """docstring for Manufacturer"""
    def make_bikes(self,number,manufacturer):
        bicycles = []
        for number in range(number):
            bicycles.append(Bicycle(manufacturer))
        return bicycles
    
    def __init__(self, manufacturer_name,margin):
        self.manufacturer_name = manufacturer_name
        self.margin = margin
        self.inventory = self.make_bikes(3,self.manufacturer_name)
        print "Margin: {:.2%}\n".format(self.margin)
        for bike in self.inventory:
            print bike
            print ""
    
    def __str__(self):
        return "{}".format(self.manufacturer_name)