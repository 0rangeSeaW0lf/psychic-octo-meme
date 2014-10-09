# from Frames import Frames
# from Wheels import Wheels

class Bicycle(object):
	"""docstring for Bicycle"""
	def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
	
	def __init__(self):
		self.model_name = self.check_input(raw_input("Model:"),chr)
		self.weight = self.check_input(raw_input("Weight:"),int)
		self.production_cost = self.check_input(raw_input("Production Cost:"),int)
		
	def __str__(self):
	    return "Model: {}\nWeight: {}".format(self.model_name,self.weight)