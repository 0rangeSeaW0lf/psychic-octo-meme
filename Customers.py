class Customer(object):
    """docstring for Customer"""
    
    def check_input(self,user_input,type_input):
        if type(user_input) == type_input:
            return user_input
        
        print("Wrong Input, please try again")
        return self.check_input(raw_input("> "),type_input)
            
    
    def __init__(self):
        self.customer_name = self.check_input(raw_input("Name:"),chr)
        self.budget = self.check_input(raw_input("Budget:"),int)
        self.bicycle = []
        
    def __str__(self):
        return "Name: {}\nCurrent Budget: {}\nOwned Bicycles: {}".format(self.customer_name,self.budget,self.bicycle)