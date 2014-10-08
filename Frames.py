class Frames(object):
	"""docstring for Frames"""
	def __init__(self,**kwargs):
		self.material = kwargs.get("material","Aluminum")
		self.weight = kwargs.get("weight",3000)
		self.production_cost = kwargs.get("production_cost",350)