from bike_manufacturer import Manufacturer

class Shop(object):
    """docstring for Bike_Shop"""
    def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
    
    def __init__(self,shop_name,markup=0.1):
        self.shop_name = shop_name
        self.markup = markup
        self.shop_inventory = {}
        self.shop_stock = 0
        self.profit = 0
        
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
                    
    def add_bike_to_stock(self,manufacturers,manufacturer,quantity):
        order = {}
        order = manufacturers[manufacturer].sell_bicycle("",quantity)
        self.shop_stock += len(order)
        for bikes in order.keys():
            self.shop_inventory["{} {}".format(manufacturer,bikes)] = order[bikes]