from boy import boy
from girl import girl
from gift import gift
from couple import couples
from generator import utility 
from generator import generate
from log import log
from random import randint
from math import exp, log10

import csv
import math
import logging
import pprint

logging.basicConfig(filename='1.log', filemode='w+', level=logging.DEBUG, format='%(asctime)s %(name)-%(levelname)s - %(message)s')

def calculate_happiness(H):
	gift = open('gifts.csv')
	gift = csv.reader(gifts, delimiter = ',')
	GIFTSLIST=[]

	GIFTSLIST = [GIFT(line[0],int(line[1]),int(line[2]),int(line[3]))for line in gift]

	gift = sorted(gift, key=lambda item:item.money)
	logging.warning('lets exchangee gifts')
	for i in H:
		if(i.boy.type == 'Miser'):
			guy_miser(gifts, i)
	
		if(i.boy.type == 'Generous'):
			guy_generous(gifts, i)


		if(i.boy.type == 'Geek'):
			guy_geek(gifts, i)

	details(H)

def happy_couple(H, k):
	A = sorted(H, key=lambda item: item.happiness, reverse=True)
	B = sorted(H, key=lambda item: item.compatibility_status, reverse=True)
	print ('\n\n' + str(k) + 'Compatible couples are:')
	for i in range(k):
		print (B[i].boy.name + ' and ' + B[i].girl.name)
		print('SAVDHAN\n')
		print ('\n\n'+str(k) + 'happy couples are:')
		for i in range(k):
			print (A[i].boy.name + ' and ' + A[i].girl.name)
			print('SAVDHAN\n')

def guy_miser(gift, m):
	g1=0
	g2=0
	for k in gift:
		if (k.money == m.girl.maintenance_budget) or (k.money-m.girl.maintenance_budget <= 100) and (m.boy.gfbudget >=0)and (m.boy.gfbudget - k.money > 0):
			if(k.type == 'Luxury'):
				g2=g2 + 2*k.money
			else:
				g2=g2 + k.money
			g1 = g1 + k.money
			m.gift = m.gift+ [k]
			m.boy.gfbudget = x.boy.gfbudget - k.money
			log(m.boy.name + 'gifted' + m.girl.name + 'gift' + k.name + '| of price = Rs.' + str(k.money) + '\-')

			if(m.girl.type == 'Choosy'):
				m.girl.happiness = log10(g2)
			elif (m.girl.type == 'Normal'):
				m.girl.happiness = g1
			else:
				m.girl.happiness = exp(g1)
	m.boy.happiness = m.boy.gfbudget
	m.happiness()
	m.compatibility()
def guy_generous(gift, m):
	g1=0
	g2=0
	for k in gift:
		if (k.money == m.girl.maintenance_budget) or (k.money-m.girl.maintenance_budget <= 100) and (m.boy.gfbudget >= 0) and (m.boy.gfbudget - k.money > 0):
			if(k.type == 'Luxury'):
				g2=g2 + 2*k.money
			else:
				g2=g2 + k.money
			g1 = g1 + k.money
		        m.gift = m.gift+ [k]
		        m.boy.gfbudget = x.boy.gfbudget - k.money
		        log(m.boy.name + 'gifted' + m.girl.name + 'gift' + k.name + '| of price = Rs.' + str(k.money) + '\-')

		if(m.girl.type == 'Choosy'):
			m.girl.happiness = log10(g2)
		elif (m.girl.type == 'Normal'):
			m.girl.happiness = g1
		else:
			m.girl.happiness = exp(g1)
	m.boy.happiness = m.girl.happiness
	m.happiness()
	m.compatibility()

def guy_geek(gift, m):
	g1=0
	g2=0
	for k in gift:
		if (k.money == m.girl.maintenance_budget) or (k.money-m.girl.maintenance_budget <= 100) and (m.boy.gfbudget >= 0) and (m.boy.gfbudget - k.money > 0):
			if(k.type == 'Luxury'):
				g2=g2 + 2*k.money
			else:
				g2=g2 + k.money
		g1 = g1 + k.money
		m.gift = m.gift + [k]
		m.boy.gfbudget = x.boy.gfbudget - k.money
		log(m.boy.name + 'gifted' + m.girl.name + 'gift' + k.name + '| of price = Rs.' + str(k.money) + '\-')

	for j in gift:
		if(j not in m.gift) and (j.type== 'Luxury') and (j.money <= m.gfbudget):
			g2 = g2 + 2*i.money
		g1 = g1 + i.money
		m.gift = m.gift + [i]
		m.boy.gfbudget = m.boy.gfbudget - i.money
		log(m.boy.name + 'gifted' + m.girl.name + 'gift' + i.name + '| of price = Rs.' + str(i.money) + '\-')	

		if(m.girl.type == 'Choosy'):
			m.girl.happiness = log10(g2)
		elif (m.girl.type == 'Normal'):
			m.girl.happiness = g1
	        else:
			m.girl.happiness = exp(g1)
	m.boy.happiness = m.girl.intelligence
	m.happiness()
	m.compatibility()

def details(H):
	for l in H:
		print ( l.girl.name + 'received gift from ' + l.boy.name )
		for i in l.gift:
			print ( i.name + 'got' + i.type + 'type of gift')
			k = randint(1, len(H))
	happy_couple(H, k)
def check():
	b = open('boys.csv')
	matchboys = csv.reader(b, delimiter = ',')
	BOYSLIST=[]
	BOYSLIST += [BOY(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),line[5])for line in matchboys]
	g =open('girls.csv')
	matchgirls = csv.reader(g, delimiter = ',')
	GIRLSLIST=[]
	GIRLSLIST +=  [GIRLS(line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),line[5])for line in matchgirls]
	COUPLELIST = []
	logging.warning('Girls are still single')
	for g in GIRLSLIST:
		for b in BOYSLIST:
			log(g.name + ' is searching ' + b.name)
			if g.status == 'single' and b.status == 'single' and g.eligibility(b.budget) and b.eligibility(g.maintenence_budget,g.attractiveness):
			     g.status = 'commited'
			     b.status = 'commited'
			     b.girlfriend = g.name
			     g.boyfriend = b.name
			     log(g.name + 'is commited with' + b.name)
			     COUPLELIST = COUPLELIST +[(b,g)]
			     break

	print('commited couples are:')
	for m in GIRLLIST :
		if m.status == 'single':
		     print(m.name + 'is single')
		else:
		    	 print(m.name + 'is commited')

	H = [couples(line[0], line[1])for line in COUPLELIST]
calculate_happiness(H)
