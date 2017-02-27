class boy:
 
	def __init__(self, name, attractiveness, intelligence, gfbudget, minimum_attraction_required,type ):
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.budget = gfbudget
		self.minimum_attraction_required = minimum_attraction_required
		self.status = 'single'
		self.girlfriend = ''
		self.type = type
		self.happiness = 0

	def happiness(self,happiness):
		self.happiness=happiness

	def girlfriend(self,girlfriend):
		self.girlfriend=girlfriend

	def eligibility(self,maintenance_budget,attractiveness):
		if(self.budget >= maintenance_budget) and (self.minimum_attraction_required <= attractiveness):
			return True
		else:
			return False
