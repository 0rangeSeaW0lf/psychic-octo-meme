from bicycle import Bicycle

class Manufacturer(object):
    """docstring for Manufacturer"""
    def make_bike(self,number,manufacturer):#,model=""):
        bicycles = {}
        #if not model:
        for number in range(number):
            while True:
                bike = Bicycle(manufacturer)
                if bike.model_name not in bicycles.keys():
                    bicycles[bike.model_name] = bike #[bike,1]
                    break
                else:
                    print("The chosen model already exists, let's try again")
                    continue
        # else:
        #     if model in bicycles.keys():
        #         bicycles[model][1] += 1
        #     else:
        #         print("Sorry that model is not produced by our company")
        return bicycles
    
    def __init__(self, manufacturer_name,margin):
        self.manufacturer_name = manufacturer_name
        self.margin = margin
        self.inventory = self.make_bike(3,self.manufacturer_name)
        print "Margin: {:.2%}\n".format(self.margin)
        for bike in self.inventory:
            print self.inventory[bike]
            print ""
    
    def __str__(self):
        return "{}".format(self.manufacturer_name)