import random

class GIFTS:
	

	utility={'W':100,'X':80,'Y':50,'Z':30}

	def __init__(self,name,price,value,category):
		self.name=name
		self.price=price
		self.value=value

		if category=='Luxury':
			self.difficult=random.randint(100)

		if category=='Utility':
			u=utility.popitem()
			self.utilityclass=u[0]
			self.utilityvalue=u[1]
