# hw due 8/14 - "financial institution"
from random import *

assets = {'cash':0}
stocks = {}
funds = {}

class Portfolio():

	def __init__(self, account='[default]'):
		self.account = account
		print 'You have successfully created a portfolio named: %s.' % (account)
		
	def addCash(self,amount):
		assets['cash'] += amount
		print 'Deposited $%s cash to your account.' % (amount)
		
	def withdrawCash(self,amount):
		if assets['cash'] - amount < 0:
			print 'Insufficient funds. Your account only contains $%s.' % (assets['cash'])
		else:
			assets['cash'] -= amount
			print 'Withdrew $%s cash from your account.' % (amount)	
	
	def buyStock(self,shares,stock):
		self.shares = int(shares)
		cost = self.shares * stock.price
		if assets['cash'] - cost >= 0:
			assets['cash'] -= cost
			stocks[stock.abbrev] += self.shares
			print 'Purchased %s shares of %s stock.' % (self.shares,stock)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)
	
	def sellStock(self,shares,stock):
		self.shares = int(shares)
		sale = self.shares * (uniform(0.5,1.5) * stock.price)
		if stock.abbrev in stocks:
			if shares <= stocks[stock.abbrev]:
				assets['cash'] += sale
				stocks[stock.abbrev] -= self.shares
				print 'Sold %s shares of %s stock.' % (self.shares,stock)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (stocks[stock.abbrev],self.shares)
		else:
			print 'This stock does not exist, or you typed the variable incorrectly.'
	
	def buyMutualFund(self,shares,fund):
		cost = shares * fund.price
		if assets['cash'] - cost >= 0:
			assets['cash'] -= cost
			funds[fund.abbrev] += shares
			print 'Purchased %s shares of the %s fund.' % (shares,fund)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)
	
	def sellMutualFund(self,shares,fund):
		sale = shares * (uniform(0.9,1.2) * fund.price)
		if fund.abbrev in funds:
			if shares <= funds[fund.abbrev]:
				assets['cash'] += sale
				funds[fund.abbrev] -= shares
				print 'Sold %s shares of the %s fund.' % (shares,fund)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (funds[fund.abbrev],shares)
		else:
			print 'This fund does not exist, or you typed the variable incorrectly.'

#### HAVE TO GET IT TO RETURN BOTH MUTUAL FUNDS AND STOCKS		
	def __str__(self):
		print 'You have $%.f in cash reserves.' % (assets['cash'])
		print 'Stocks: '
		for i in stocks,funds:
			return i + '--> ' + str(stocks[i]) + ' shares.'
		print 'Mutual Funds: '
		for j in funds:
			print j + '--> ' + str(funds[j]) + ' shares.'
				
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

	

# functionality requirements

# complete
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH 
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
portfolio.withdrawCash(50) #Removes $50
portfolio.sellMutualFund("BRT", 3) 

# incomplete
print(portfolio) 
portfolio.history() #Prints a list of all transactions ordered by time
  




