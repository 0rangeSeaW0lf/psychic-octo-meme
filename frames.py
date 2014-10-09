class Frames(object):
	"""docstring for Frames"""
	
	def choose_frame(self,frames):
		options = frames.keys()
		i = 1
		for option in options:
			print "{}. Material: {}".format(i,option)
			print "   Weight: {} g\n   Production Cost: EUR {}\n".format(frames[option]["weight"], frames[option]["cost"])
			i += 1
			
		user_input = raw_input("Which frame do you want to choose? ")
		print("")
		if isinstance(int(user_input),int) and user_input > 0 and int(user_input) <= i:
			user_input = int(user_input)
			return options[user_input-1]
		else:
			print("Please choose a valid option!\n")
			return self.choose_frame(frames)

	def __init__(self):
		frames = {'Aluminum': {'cost': 250, 'weight': 1432}, 'Steel': {'cost': 100, 'weight': 2725},'Carbon': {'cost': 500, 'weight': 1340, 'type':"Track"}}
		self.frame_material = self.choose_frame(frames)
		self.frame_weight = frames[self.frame_material]["weight"]
		self.frame_cost = frames[self.frame_material]["cost"]
		
	def __str__(self):
		return "Material: {}\nWeight (g): {}\n".format(self.frame_material,self.frame_weight)