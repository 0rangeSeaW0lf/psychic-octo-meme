from frames import Frames
from wheels import Wheels

class Bicycle(object):
	"""docstring for Bicycle"""
	def check_input(self,user_input,type_input):
	    if type(user_input) == type_input:
	        return user_input
	
	def __init__(self):#(self,manufacturer):
		self.frame = Frames()
		self.wheels = Wheels()
		#self.manufacturer = manufacturer
		self.model_name = "Hola"
		self.weight = (self.frame.frame_weight + 2 * self.wheels.wheel_weight)/1000.0
		self.cost = self.frame.frame_cost + 2 * self.wheels.wheel_cost
		
	def __str__(self):
	    return "Model: {}\nWeight: {:.2f} Kg\nFrame: {}\nWheels: {}\n".format(self.model_name,self.weight,self.frame.frame_material,self.wheels.wheel_model)