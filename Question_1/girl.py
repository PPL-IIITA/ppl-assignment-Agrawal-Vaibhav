class girl:

	def __init__(self, name, attractiveness, intelligence, maintenance_budget):
		#defining attributes of girl
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.maintenance_budget = maintenance_budget
		self.status = 'single'
		self.boyfriend = ''
	#defining eligibility criteria for girl
	def eligibility(self,budget):
		if(self.maintenance_budget <= budget):
			return True
		else:
			return False
