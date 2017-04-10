from boy import BOY
from girl import GIRL
from gift import GIFTS
from couples import COUPLE
from datetime import datetime
import operator
import random
import csv
import math
import sys


Gifts=['essential','luxury','utility']
Boys=['Avinash','Abhishek','Kunal','Shashak','Saurav','Ankit','Jadu','Jangbahadur','Akhilesh','Amar','Akbar','Saras','Lolo','Dange','Ali','Mohammad']
Girls=['Adah','Gulson','Nina','Veronica','Sanika','Neha','Pooja','Ankita','Sandhya']
btype=['miser','generous','geeks']
gtype=['choosy','normal','desperate']
criteria=['most rich','most intelligent','most attractive']

commited=[]
B=[]
G=[]
guylist=[]
girllist=[]
couplesList=[]
giftlist=[]

guylist = open('guy.csv')
	gift = csv.reader(guy, delimiter = ',')
	GUYSSLIST=[]
girllist = open('girl.csv')
	gift = csv.reader(girl, delimiter = ',')
	GIRLSLIST=[]
file=open("log.txt","w")
for item in commited:
	file.write(str(datetime.now()))
file.write(" %s\n"%item)

for i in range(16):
	b=BOY(boys[i],random.randint(20,100),random.randint(34,100),random.randint(50,500),random.randint(9,50),random.choice(btype))
	guylist.append([b.name,b.attraction,b.intelligent,b.budget,b.minatr,b.type,b.status])
	B.append(b)

B.sort(key=lambda x:x,attraction)

for i in range(9):
	g=GIRL(girls[i],andom.randint(34,100),random.randint(50,500),random.randint(9,50),random.choice(criteria),random.choice(gtype))
	girllist.append([g.name,g.attraction,g.intelligent,g.mainbudget,g.criteria,g.type,g.status])
	G.append(g)

G.sort(key=lambda x:x,attraction)


def FINDDATES():
	for boy in B:
		for girl in G:
			if boy.pairing(girl) and girl.repairing(boy) and boy.currentstatus()=='single' and girl.currentstatus()=='single':
				boy.statuschange()
				girl.statuschange()
				c=COUPLE(boy.name,boy.type,girl.type,girl.name,boy.budget,girl.maintbudget,boy.attraction,girl.attraction,boy.intelligent,girl.intelligent)
				couplesList.append(c)
				s1=boy.name+'date'+girl.name
				commited.append(s1)
				break
				i=i+1
				G.remove(girl)
				B.remove(boy)
				break
			if i%2!=0:
				break

		else:
			for girl in G:
				for boy in B:
			if boy.pairing(girl) and girl.repairing(boy) and boy.currentstatus()=='single' and girl.currentstatus()=='single':
				boy.statuschange()
				girl.statuschange()
				c=COUPLE(boy.name,boy.type,girl.type,girl.name,boy.budget,girl.maintbudget,boy.attraction,girl.attraction,boy.intelligent,girl.intelligent)
				couplesList.append(c)
				s1=boy.name+'date'+girl.name
				commited.append(s1)
				G.remove(girl)
				B.remove(boy)
				i=i+1
				break
			if i%2!=0:
				break
 FINDDATES():


s1='It is time to start'
commited.append(s1)

giftBasket=[]

gft=['Charger',' Camera','Book','Chocolate','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
for item in gft:
	giftBasket.append(gifts(item,random.randint(50,3500),random.randint(1,100),random.choice(gifts)))

giftBasket.sort(key=operator.attrgetter('price'))

fate=[]
happyCouples={}
compatibleCouples={}

for c in CouplesList:

	x1=0
	y1=0
	
	before=c.budget
	money=0
	for item in giftBasket:
		if before<=0 or money>=c.maintbudget:
			break
		before-=item.price
		c.priceTag.append(item.price)
		c.valueTag.append(item.value)
		spent+=item.price
		s1=c.bf+' gifts '+item.name+' '+c.gf
		commited.append(s1)
	c.Cal(c.budget,money)
	x1=c.happiness
	y1=c.compatibility
	z=(x1,y1)
	fate.append(z) 
	happyCouples.update({(c.boyfriend,c.girlfriend):x1}
	compatibleCouples.update({(c.boyfriend,c.girlfriend):y1})

singlegirl=[]
singleboy=[]

fate.sort(key=lambda x:x[0],reverse=True)
k=3
s1=str(k)+' least happiest couples are'
commit.append(s1)
print(s1)

xi=[x[0] for x in fate]
topk=hi[-k:]
for item in topk:
	s1=list(happyCouples.keys())[list(happyCouples.values()).index(item)][0]
	s2=list(happyCouples.keys())[list(happyCouples.values()).index(item)][1]
	s3= s1+' and '+ s2+' with happiness value: '+str(item)
	commited.append(s3)
	print(s3)	
	singleboy.append(s1)
	singlegirl.append(s2)

print('\n')



