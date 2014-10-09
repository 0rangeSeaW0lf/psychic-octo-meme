class Wheels(object):
	"""docstring for Wheels"""
	
	def choose_wheel(self,wheels):
		options = wheels.keys()
		i = 1
		for option in options:
			print "{}. Model Name: {}".format(i,option)
			print "   Weight: {} g\n   Production Cost: EUR {}\n".format(wheels[option]["weight"], wheels[option]["cost"])
			i += 1
			
		user_input = raw_input("Which wheels do you want to choose? ")
		print("")
		if isinstance(int(user_input),int) and user_input > 0 and int(user_input) <= i:
			user_input = int(user_input)
			return options[user_input-1]
		else:
			print("Please choose a valid option!\n")
			return self.choose_wheel(wheels)

	def __init__(self):
		wheels = {'Torch': {'cost': 120, 'weight': 890}, 'Mavic': {'cost': 190, 'weight': 685},'Zipp': {'cost': 95, 'weight': 865}}
		self.wheel_model = self.choose_wheel(wheels)
		self.wheel_weight = wheels[self.wheel_model]["weight"]
		self.wheel_cost = wheels[self.wheel_model]["cost"]
		
	def __str__(self):
		return "Model: {0}\nWeight (g): {1}\n".format(self.wheel_model,self.wheel_weight)