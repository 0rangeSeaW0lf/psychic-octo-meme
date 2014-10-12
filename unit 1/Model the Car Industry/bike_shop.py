from bike_manufacturer import Manufacturer

class Shop(object):
    """docstring for Bike_Shop"""
    def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
    
    def __init__(self,shop_name,suppliers = {},markup=0.2):
        self.shop_name = shop_name
        self.markup = markup
        self.shop_inventory = {}
        self.shop_stock = 0
        self.profit = 0
        self.suppliers = suppliers
        
    def __str__(self):
        return "{}".format(self.shop_name)
        
    def order_bicycle(self,manufacturers = {},quantity="3"):
        if not manufacturers:
            manufacturer_names = manufacturers.keys()
            i = 1
            for manufacturer in manufacturer_names:
                print "{}. {}".format(i,manufacturer)
            user_input = ("From which company do you want to buy bicycles?")
            if user_input.isdigit() and int(user_input) > 0:
                manufacturer = manufacturer_names[int(user_input)-1]
                self.add_bike_to_stock(manufacturers,manufacturer,quantity)
            else:
                print("Sorry, wrong input. Please try again")
                return self.order_bicycle(manufacturers,quantity)
        else:
            for manufacturer in manufacturers:
                self.add_bike_to_stock(manufacturers,manufacturer,quantity)
            
            i,j = 0,0
            
            for bike in self.shop_inventory:
                if self.shop_inventory[bike].cost < 200:
                    i += 1
                elif self.shop_inventory[bike].cost > 500:
                    j += 1
                    
            if i < 1:
                return self.order_bicycle(self.suppliers,"1")
            elif j < 1:
                return self.order_bicycle(self.suppliers,"1")
                
    def add_bike_to_stock(self,manufacturers,manufacturer,quantity):
        order = {}
        order = manufacturers[manufacturer].sell_bicycle("",quantity)
        self.shop_stock += len(order)
        for bikes in order.keys():
            self.shop_inventory["{} {}".format(manufacturer,bikes)] = order[bikes]
    
    def sell_bicycle(self,budget,customer):
        options = {}
        keys  = self.shop_inventory.keys()
        option = []
        i = 1
        print("\nAvailable Options\n=================")
        for bike in keys:
            if self.shop_inventory[bike].cost <= budget:
                options[bike] = self.shop_inventory[bike]
                print("{}.".format(i))
                print self.shop_inventory[bike]
                print "Price: EUR {}\n".format(self.shop_inventory[bike].cost)
                option.append(bike)
                i += 1
        if not options:
            print("Sorry, we ran out of bicycles")
            return
        else:
            if i == 1:
                pass
            else:
                user_input = raw_input("Which bike do you want to buy? ")
                if user_input.isdigit() and user_input > 1 and int(user_input) <= i:
                    user_input = int(user_input) - 1
                    bike = option[user_input]
                else:
                    # All customers must be able to have at least one option to choose
                    return self.sell_bicycle(budget,customer)
            customer.bicycle = {bike:options[bike]}
            customer.budget -= options[bike].cost
            self.profit += int(options[bike].cost * self.markup / (1 + self.markup))
            self.shop_stock -= 1
            del self.shop_inventory[bike]
            
        
    def show_inventory(self):
        if not self.shop_inventory:
            print("Out of stock")
        else:
            print("INVENTORY\n=========\n")
            for bike in self.shop_inventory:
                print self.shop_inventory[bike]
                print "Price: EUR {}\n".format(self.shop_inventory[bike].cost)