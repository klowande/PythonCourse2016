# hw due 8/14 - "financial institution"
from random import *

assets = {'cash':0}
stocks = {}
funds = {}
log = []

class Portfolio():

	def __init__(self, account='[default]'):
		self.account = account
		x = 'You have successfully created a portfolio named: %s.' % (account)
		self.track(x)
	
	def track(self,transaction):
		print transaction
		log.append(transaction)
		
	def addCash(self,amount):
		assets['cash'] += amount
		x = 'Deposited $%s cash to your account.' % (amount)
		self.track(x)
		
	def withdrawCash(self,amount):
		if assets['cash'] - amount < 0:
			print 'Insufficient funds. Your account only contains $%s.' % (assets['cash'])
		else:
			assets['cash'] -= amount
			x = 'Withdrew $%s cash from your account.' % (amount)	
			self.track(x)
			
	def buyStock(self,shares,stock):
		self.shares = int(shares)
		cost = self.shares * stock.price
		if assets['cash'] - cost >= 0:
			assets['cash'] -= cost
			stocks[stock.abbrev] += self.shares
			x = 'Purchased %s shares of %s stock.' % (self.shares,stock)
			self.track(x)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)
	
	def sellStock(self,shares,stock):
		self.shares = int(shares)
		sale = self.shares * (uniform(0.5,1.5) * stock.price)
		if stock.abbrev in stocks:
			if shares <= stocks[stock.abbrev]:
				assets['cash'] += sale
				stocks[stock.abbrev] -= self.shares
				x = 'Sold %s shares of %s stock.' % (self.shares,stock)
				self.track(x)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (stocks[stock.abbrev],self.shares)
		else:
			print 'This stock does not exist, or you typed the variable incorrectly.'
	
	def buyMutualFund(self,shares,fund):
		cost = shares * fund.price
		if assets['cash'] - cost >= 0:
			assets['cash'] -= cost
			funds[fund.abbrev] += shares
			x = 'Purchased %s shares of the %s fund.' % (shares,fund)
			self.track(x)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)
	
	def sellMutualFund(self,shares,fund):
		sale = shares * (uniform(0.9,1.2) * fund.price)
		if fund.abbrev in funds:
			if shares <= funds[fund.abbrev]:
				assets['cash'] += sale
				funds[fund.abbrev] -= shares
				x = 'Sold %s shares of the %s fund.' % (shares,fund)
				self.track(x)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (funds[fund.abbrev],shares)
		else:
			print 'This fund does not exist, or you typed the variable incorrectly.'
	
	def history(self):
		print 'Transaction History:'
		for j in log:
			print j	
		
	def __str__(self):
		return """You have $%.f in cash reserves.
You own the following stocks:\n%s 
You own the following mutual funds:\n%s""" % (assets['cash'],stocks,funds)
				
class Stock():
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		stocks[abbrev] = 0
		print 'Created the stock %s with share price: $%s.' % (abbrev,price)		
	def __repr__(self):
		return self.abbrev

class MutualFund():
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		funds[abbrev] = 0
		print 'Created the %s fund with share price: $%s.' % (abbrev,price)		
	def __repr__(self):
		return self.abbrev					

########## test code
a=Portfolio()
a.addCash(500)
s=Stock(5,"STO")
a.buyStock(25,s)
a.sellStock(5,s)
q=MutualFund(800,"VTMX")
a.buyMutualFund(0.16,q)
a.sellMutualFund(0.12,q)
a.sellMutualFund(1,q)
print a
a.history()
  




