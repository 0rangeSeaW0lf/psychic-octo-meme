from bike_shop import Shop
from bicycle import Bicycle

class Customer(object):
    """docstring for Customer"""
    
    def check_input(self,user_input,type_input):
        if type_input == int:
            if user_input.isdigit():
                user_input = int(user_input)
                
        if isinstance(user_input,type_input):
            return user_input
        else:
            print("Wrong input, please try again\n")
            self.check_input(raw_input("> "),type_input)
            
    
    def __init__(self,name = "", budget = ""):
        if not name:
            name = self.check_input(raw_input("Name: "),str)
        self.customer_name = name
        if not budget:
            budget = self.check_input(raw_input("Budget: "),str)
        self.budget = int(budget)
        self.bicycle = {}
        
    def __str__(self):
        return "Name: {}\nBudget: EUR {}\nOwned Bicycles: {}\n".format(self.customer_name,self.budget,"".join(self.bicycle.keys()))
        
    def buy_bicycle(self,bike_shop):
        bike_shop.sell_bicycle(self.budget,self)