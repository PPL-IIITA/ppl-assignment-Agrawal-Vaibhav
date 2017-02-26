class boy:
 
	def __init__(self, name, attractiveness, intelligence, gfbudget, minimum_attraction_required ):
		#defining attributes of boy
		self.name = name
		self.attractiveness = attractiveness
		self.intelligence = intelligence
		self.budget = gfbudget
		self.minimum_attraction_required = minimum_attraction_required
		self.status = 'single'
		self.girlfriend = ''

	#defining eligibility criteria for boy

	def eligibility(self,maintenance_budget,attractiveness):
		if(self.budget >= maintenance_budget) and (self.minimum_attraction_required <= attractiveness):
			return True
		else:
			return False
