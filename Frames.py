class Frames(object):
	"""docstring for Frames"""
	def choose_frame(self,wheels):
		options = wheels.keys()
		i = 1
		for option in options:
			print "{}. Model Name: {}".format(i,option)
			print "   Material: {}\n   Weight(g): {}\n   Production Cost(EUR): {}\n".format(wheels[option]["material"], wheels[option]["weight"], wheels[option]["cost"])
			i += 1
			
		user_input = raw_input("Which wheel do you want to choose? ")
		print("")
		if isinstance(int(user_input),int) and user_input > 0 and int(user_input) <= i:
			user_input = int(user_input)
			return options[user_input-1]
		else:
			print("Please choose a valid option!\n")
			return self.choose_frame(wheels)

	def __init__(self):
		frames = {'Aluminum': {'cost': 150, 'weight': 890}, 'Steel': {'cost': 50, 'weight': 2725},'Carbon': {'cost': 500, 'weight': 865, 'type':"Track"}}
		self.material = self.choose_frame(frames)
		self.weight_frame = frames[self.material]["weight"]
		self.cost_frame = frames[self.material]["cost"]
		
	def __str__(self):
		return "Material: {}\nWeight (g): {}\n".format(self.material,self.weight_frame)