from bike_manufacturer import Manufacturer

class Bike_Shop(object):
    """docstring for Bike_Shop"""
    def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
    
    def __init__(self):
        self.shop_name = self.check_input(raw_input("Shop Name:"),chr)
        self.shop_inventory = {}
        self.shop_stock = 0
        self.profit = 0
        self.markup = 0.2
        
    def __str__(self):
        return "{}".format(self.shop_name)
        
    def order_bicycle(self,manufacturers = {},quantity="3"):
        order = {}
        if not manufacturers:
            i = 1
            for manufacturer in manufacturers.keys():
                print "{}. {}".format(i,manufacturer)
            user_input = ("From which company do you want to buy bicycles?")
        else:
            for manufacturer in manufacturers:
                order = manufacturer.sell_bicycle("",quantity)
                self.shop_stock += len(order)
                for bikes in order.keys():
                    self.shop_inventory["{} {}".format(manufacturer,bik)] = order[bikes]