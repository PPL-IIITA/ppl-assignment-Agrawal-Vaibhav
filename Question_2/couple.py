class couples:
	
	def __init__(self,girl,boy):
		self.girl=girl
		self.boy=boy
		self.happiness=0
		self.gift=[]
		self.compatibility=0

	def happiness(self):
		self.happiness = self.boy.happiness + self.girl.happiness
 
	def compatibility(self):
		x=self.boy.gfbudget - self.girl.maintenance_budget
		y=abs(self.boy.attractiveness - self.girl.attractiveness)
		z=abs(self.boy.intelligence - self.girl.intelligence)
		
		self.compatibility = x+y+z

