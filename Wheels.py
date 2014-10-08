class Wheels(object):
	"""docstring for Wheels"""
	def __init__(self, **kwargs):
		self.material = kwargs.get("model_name","Aluminum")
		self.weight = kwargs.get("weight",3000)
		self.production_cost = kwargs.get("production_cost",350)
