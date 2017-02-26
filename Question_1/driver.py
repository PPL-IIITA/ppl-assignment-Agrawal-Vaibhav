from boy import boy
from girl import girl
from generate import utility 
from log import log
import csv
utility()
b = open('boys.csv')
matchboys = csv.reader(b, delimiter = ',')
BOYSLIST=[]
g =open('girls.csv')
matchgirls = csv.reader(g, delimiter = ',')
GIRLSLIST=[]

BOYSLIST = [boy(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]))for line in matchboys]

GIRLSLIST =  [girl(line[0],int(line[1]),int(line[2]),int(line[3]))for line in matchgirls]
	
for g in GIRLSLIST:
	for b in BOYSLIST:
		log(g.name + ' is searching ' + b.name)
		if g.status == 'single' and b.status == 'single' and g.eligibility(b.budget) and b.eligibility(g.maintenance_budget,g.attractiveness):
			g.status = 'commited'
			b.status = 'commited'
			b.girlfriend = g.name
			g.boyfriend = b.name
			print(g.name + 'is commited with' + b.name)
			log(g.name + 'is commited with' + b.name)
			break
