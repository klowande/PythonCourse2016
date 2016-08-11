# hw due 8/14 - "financial institution"

assets = {'cash':0}
stocks = {}

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
		cost = shares * stock.price
		if assets['cash'] - cost >= 0:
			assets['cash'] -= cost
			stocks[stock.abbrev] += shares
			print 'Purchased %s shares of %s stock.' % (shares,stock)
		else:
			print 'Insufficient funds. Cash reserve at $%s, transaction requires $%s.' % (assets['cash'],cost)
	
	def sellStock(self,shares,stock):
		sale = shares * stock.price
		if stock.abbrev in stocks:
			if shares <= stocks[stock.abbrev]:
				assets['cash'] += sale
				stocks[stock.abbrev] -= shares
				print 'Sold %s shares of %s stock.' % (shares,stock)
			else:
				print 'Insufficient shares. You own %s; you tried to sell %s.' % (stocks[stock.abbrev],shares)
		else:
			print 'This stock does not exist, or typed the variable incorrectly.'
			
class Stock():
	def __init__(self,price,abbrev):
		self.price=price
		self.abbrev=abbrev
		stocks[abbrev] = 0
		print 'Created the stock %s with share price: $%s.' % (abbrev,price)		
	def __repr__(self):
		return self.abbrev
					
	
	
##########
	
	def buyMutualFund(self,shares,mf):
		self.shares = shares
		if mf in allmfs:
			print 'Purchased %s shares of the %s fund.' % (shares,mf)
		else:
			print """Error: The ticker symbol you provided does not yet exist.
You must first create the fund with 'MutualFund()'."""
	
	def sellMutualFund(self,shares,mf):
		self.shares = shares
		if mf in allmfs:
			print 'Sold %s shares of the %s fund.' % (shares,mf)
		else:
			print """Error: The ticker symbol you provided does not yet exist.
You must first create the fund with 'MutualFund()'."""
		
		
class MutualFund(product):
	def __init__(self,abbrev):
		self.abbrev=abbrev
		allmfs.append(self.abbrev)
		print 'Created the %s fund.' % (abbrev)
		
# functionality requirements

# complete
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s

mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
portfolio.withdrawCash(50) #Removes $50

# incomplete
print(portfolio) 
#Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT 
# 2GHT 

portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT 
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH 
portfolio.history() #Prints a list of all transactions ordered by time
  
# additional not-required functionality:
# retire: probabilistically determine amount of retirement savings
# and number of years until insolvency.



