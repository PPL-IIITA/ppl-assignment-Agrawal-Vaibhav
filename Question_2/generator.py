import csv
from random import randint
from random import choice
def utility():
	boytype = ['Miser','Generous','Geek']
	girltype = ['Choosy','Normal','Desperate']
	gifttype = ['Essential','Luxury','Utiltiy']
		
	b=[]
	g=[]
	gift=[]
	for i in range(0,50):
		b+=[('BOY'+str(i),randint(0,50),randint(0,50),randint(0,50),randint(0,50),boytype[randint(0,2)])]

	for j in range(0,20):
		g+=['GIRL'+str(j),randint(0,20),randint(0,20),randint(0,20),girltype[randint(0,2)]]

	for k in range(0,10):
		gift+=['GIFT'+str(k),randint(0,10),randint(0,10),gifttype[randint(0,2)]]


generate('boys.csv' ,b)
generate('girls.csv' ,g)
generate('gifts.csv' ,gift)

def generate(file,data):
	f = open(file,'wr')
	writer = csv.writer(f, delimiter = ',')

	for lines in data:
		writer.writerow(lines)
