class Wheels(object):
	"""docstring for Wheels"""
	
	def choose_wheel(self,wheels):
		options = wheels.keys()
		i = 1
		for option in options:
			print "{}. Model Name: {}".format(i,option)
			print "   Type: {}\n   Weight(g): {}\n   Production Cost(EUR): {}\n".format(wheels[option]["type"], wheels[option]["weight"], wheels[option]["cost"])
			i += 1
			
		user_input = raw_input("Which wheel do you want to choose? ")
		print("")
		if isinstance(int(user_input),int) and user_input > 0 and int(user_input) <= i:
			user_input = int(user_input)
			return options[user_input-1]
		else:
			print("Please choose a valid option!\n")
			return self.choose_wheel(wheels)

	def __init__(self):
		wheels = {'Torch': {'cost': 120, 'weight': 890,'type':"Mountain"}, 'Mavic': {'cost': 190, 'weight': 685, 'type':"Road"},'Zipp': {'cost': 95, 'weight': 865, 'type':"Track"}}
		self.model_name = self.choose_wheel(wheels)
		self.wheel_type = wheels[self.model_name]["type"]
		self.weight_wheel = wheels[self.model_name]["weight"]
		self.production_cost = wheels[self.model_name]["cost"]
		
	def __str__(self):
		return "Model: {0}\nType: {2}\nWeight (g): {1}\n".format(self.model_name,self.weight_wheel,self.wheel_type)