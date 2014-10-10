from bicycle import Bicycle

class Manufacturer(object):
    """docstring for Manufacturer"""
    # Procedure to manufacture bicycles
    
    def __init__(self, manufacturer_name,margin,bikes=3):
        self.manufacturer_name = manufacturer_name
        self.margin = margin
        self.inventory = self.make_bike(bikes)
        # for bike in self.inventory:
        #     print self.inventory[bike]
        #     print ""
    def __str__(self):
        return "{}".format(self.manufacturer_name)
        
    def make_bike(self,number,manufacturer="",margin=""):
        if not manufacturer:
            manufacturer = self.manufacturer_name
        if not margin:
            margin = self.margin
            
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
                    # print("The chosen model already exists, let's try again")
                    continue
        return bicycles
    
    def sell_bicycle(self,inventory=""):
        if not inventory:
            inventory = self.inventory
            
        if inventory:
            options = inventory.keys()
            i = 1
            print("\nAvailable Stock\n===============\n")
            for bike in self.inventory:
                print "{}.".format(i),
                print self.inventory[bike]
                print ""
                i += 1
            
            user_input = raw_input("Which bicycle do you want to order? ")
            print("")
            
            if user_input.isdigit() and user_input > 0 and int(user_input) < i:
                user_input = int(user_input)
                bike = inventory[options[user_input-1]]
                del inventory[options[user_input-1]]
                return bike
            else:
                print("Please choose a valid option!\n")
                return self.sell_bicycle()
        else:
            print("Sorry! We ran out of bicycles. Come back tomorrow!")
            
           