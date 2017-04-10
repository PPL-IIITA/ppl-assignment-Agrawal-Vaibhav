class BOY:

	def __init__(self,name,attraction,intelligent,budget,minatr,type,status='single'):
		self.name=name
		self.attraction=attraction
		self.intelligent=intelligent
		self.budget=budget
		self.minatr=minatrself.status
		self.type=type
		self.status=status


	def pairing(self,girl):
		if self.budget>=girl.mainbudget and self.minatr<=attraction:
			return True
		return False

	def currentstatus(self):
		return self.status

	def statuschange(self):
		if self.status=='commited':
			self.status='single'
		else:
			self.status='commited'
