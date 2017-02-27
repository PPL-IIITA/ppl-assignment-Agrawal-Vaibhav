class girl:

	def __init__(self, name, attractiveness, intelligence, maintenance_budget, type):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.maintenance_budget = maintenance_budget
		self.status = 'single'
		self.boyfriend = ''
		self.type = type
		self.happiness = 0

	def happiness(self,happiness):
		self.happiness=happiness

	def girlfriend(self,girlfriend):
		self.girlfriend=girlfriend

	def eligiblity(self,budget):
		if(self.maintenance_budget <= budget):
			return True
		else:
			return False
