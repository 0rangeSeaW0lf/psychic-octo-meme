class Bike_Shop(object):
    """docstring for Bike_Shop"""
    def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
    
    def __init__(self):
        self.shop_name = self.check_input(raw_input("Shop Name:"),chr)
        self.inventory = {}
        self.stock = 0
        self.profit = 0
        self.markup = 0.2
        
    def __str__(self):
        return "{}".format(self.shop_name)
        
    def inventory_management(self,bicycle):
            self.stock += 1
            self.inventory[bicycle.model_name] = bicycle
    
    def sell_bicycle(self,customer):
        option = []
        if not self.inventory:
            for bike,number in self.inventory,range(1,len(self.inventory)+1):
                option += [number,bike]
                print("{}.\n{}".format(number,self.inventory[bike]))
                price = self.inventory[bike].production_cost * (1 + self.markup)
                print("Price: EUR {}".format(price))
                print("{}. None".format(len(self.inventory)+1))
            while True:
                customer_choice = raw_input("Which bicycle do you want?")
                if type(customer_choice) == int and customer_choice > 0 and customer_choice < (len(customer_choice) + 2):
                    customer_choice = int(customer_choice)
                    if customer_choice == len(customer_choice) + 1:
                        break
                    else:
                        self.stock -= 1
                        self.inventory[option[customer_choice-1][1]]
                else:
                    print("Please, choose a valid option!")
        else:
            print("Sorry, we ran out of bikes. Come back tomorrow!")