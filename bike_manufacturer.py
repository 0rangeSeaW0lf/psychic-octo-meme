from bicycle import Bicycle

class Manufacturer(object):
    """docstring for Manufacturer"""
    # Procedure to manufacture bicycles
    
    def __init__(self, manufacturer_name,margin=0.1,bikes=3):
        self.manufacturer_name = manufacturer_name
        self.margin = margin
        self.inventory = self.make_bike(bikes)
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
                    continue
        return bicycles
    
    def sell_bicycle(self,inventory="", no_bikes = "0"):
        if not inventory:
            inventory = self.inventory
            
        if inventory:
            order = {}
            options = inventory.keys()
            if no_bikes.isdigit() and int(no_bikes) > 0:
                no_bikes = int(no_bikes)
                if no_bikes <= len(inventory):
                    for bike_num in range(no_bikes):
                        order[options[bike_num]] = self.inventory[options[bike_num]]
                    return order
                else:
                    print("Sorry, the manufacturer does not have {} in stock (Current stock: {})".format(no_bikes,len(inventory)))
                    while True:
                        confirmation = raw_input("Do you still want to place an order with less items? (yes/no) ").lower()
                        if confirmation == "yes":
                            return self.sell_bicycle("",raw_input("How many bicycles (max. {})? ".format(len(inventory))))
                        elif confirmation == "no":
                            return
                        else:
                            print("Wrong input! Valid option \"yes\" or \"no\". Please try again")
            else:
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
                    order[options[user_input-1]] = inventory[options[user_input-1]]
                    del inventory[options[user_input-1]]
                    return bike
                else:
                    print("Please choose a valid option!\n")
                    return self.sell_bicycle()
        else:
            print("Sorry! The manufacturer ran out of bicycles. Come back tomorrow!")