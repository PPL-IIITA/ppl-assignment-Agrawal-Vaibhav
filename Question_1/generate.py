import csv
from random import randint

def utility():
	b = []
	g = []
	for i in range(0,50):
		b+=[('BOY'+str(i),randint(5,50),randint(6,50),randint(10,50),randint(5,50))]

	for j in range(0,20):
		g+=[('GIRL'+str(j),randint(7,50),randint(9,30),randint(13,30))]

	generate('boys.csv' ,b)
	generate('girls.csv' ,g)

def generate(file,data):
	f = open(file,'wr')
	writer = csv.writer(f, delimiter = ',')

	for lines in data:
		writer.writerow(lines)
