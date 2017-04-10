import math
class COUPLE:

def __init__(self,boyfriend,boyfriendtype,girlfriendtype,girlfriend,budget,mainbudget,boyfriendattraction,girlfriendattraction,boyfriendint,girlfriendint):
	self.boyfriend=boyfriend
	self.boyfriendtype=boyfriendtype
	self.girlfriendtype=girlfriendtype
	self.girlfriend=girlfriend
	self.budget=budget
	self.mainbudget=mainbudget
	self.boyfriendattraction=boyfriendattraction
	self.girlfriendattraction=girlfriendattraction
	self.boyfriendint=boyfriendint
	self.girlfriendint=girlfriendint



	pricetag=[]
	valuetag=[]
	happiness=0
	compatibility=0

	def cal(self,before,spent):

		self.happiness=abs(before-spent)
		self.compatibility=abs(before-spent)+abs(self.boyfriendattraction-self.girlfriendattraction)+abs(self.boyfriendint-self.girlfriendint)

		if self.boyfriendtype=='generous':
			if self.girlfriendtype=='choosy':
				self.happiness+=math.log(sum(self.priceTag),2)
			elif self.girlfriendtype=='normal':
				self.happiness+=sum(self.priceTag)+sum(self.valueTag)
			else:
self.happiness+=(sum(self.priceTag))**2


		
		elif self.boyfriendtype=='miser':
			if self.girlfriendtype=='choosy':
				self.happiness+=math.log(sum(self.priceTag),2)			
			elif self.girlfriendtype=='normal':
				self.happiness+=sum(self.priceTag)+sum(self.valueTag)
			else:
				self.happiness+=(sum(self.priceTag))**2

		else:
		if self.girlfriendtype=='choosy':
			self.happiness+=math.log(sum(self.pricetag),2)

		elif self.girlfriendtype=='normal':
			self.happiness+=sum(self.pricetag)+sum(self.valuetag)

		else:
			self.happiness+=(sum(self.pricetag))**2


