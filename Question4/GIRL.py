class GIRL:
	
	def __init__(self,name,attraction,intelligent,mainbudget,criteria,type,status='single'):
		self.name=name
		self.attraction=attraction
		self.mainbudget=mainbudget
		self.intelligent=intelligent
		self.criteria=criteria
		self.type=type
		self.status=status

	def pairing(self,boy):
		if boy.budget<self.mainbudget and self.status=='commited'
			return False
		return True

	def currentstatus(self):
		return self.status

	def statuschange(self):
		if self.status=='commited':
			self.status='single'
		else:
			self.status='commited'
