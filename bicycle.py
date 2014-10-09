from random import choice
from frames import Frames
from wheels import Wheels

class Bicycle(object):
	"""docstring for Bicycle"""
	def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
	
	def __init__(self, manufacturer):
		# the names list contains model from Specialized bikes as I am a huge fan of its bikes (I own one! :-))
		names = ["Pitch", "Epic", "Source", "Enduro", "Fatboy", "Status", "Demo", "Tarmac", "Allez", "Venge", "Shiv", "Roubaix", "Secteur", "Diverge", "Awol", "Crux", "Langster", "Sirrus", "Daily", "Crosstail", "CossRoads", "Expedition"]
		self.frame = Frames()
		self.wheels = Wheels()
		self.manufacturer = manufacturer
		self.model_name = choice(names)
		self.weight = (self.frame.frame_weight + 2 * self.wheels.wheel_weight)/1000.0
		self.cost = self.frame.frame_cost + 2 * self.wheels.wheel_cost
		
	def __str__(self):
	    return "Manufacturer: {}\nModel: {}\nWeight: {:.2f} Kg\nFrame: {}\nWheels: {}\n".format(self.manufacturer ,self.model_name,self.weight,self.frame.frame_material,self.wheels.wheel_model)