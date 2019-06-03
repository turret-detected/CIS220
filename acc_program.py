#Acct. Program prototype
#By: Andrew Mohnkern

#Class def
class FinancialAccount:

	idList = []

	def __init__(self, name, accnum, amount=0):
		self.name = name
		self.amount = amount
		self.accnum = accnum
		self.idList.append(accnum)
		
	def giveCredit(self, amountC):
		self.amount = self.amount - amountC
		
	def giveDebit(self, amountD):
		self.amount = self.amount + amountD
		
	def returnAmount(self):
		return self.amount
		
	def returnName(self):
		return self.name
		
	def returnAccNum(self):
		return self.accnum
		
	def outNeat(self):
		print(str(self.returnName())+ " " + str(self.returnAccNum()) + ": $" + str(self.returnAmount()))
		
		
#Chart of Accounts		
a1000 = FinancialAccount("Cash", 1000)
a1101 = FinancialAccount("Acc. Receivable Sars", 1101)
a1102 = FinancialAccount("Acc. Receivable H1N1", 1102)
a1200 = FinancialAccount("Office Building", 1200)

a2200 = FinancialAccount("Staples CC Due", 2200)

a3000 = FinancialAccount("Contributed Capital", 3000)

a4000 = FinancialAccount("Salaries Expense", 4000)

a5000 = FinancialAccount("Projects Completed", 5000)

#Do transaction
def createTransaction(creditAcc, debitAcc, amount): #should be class names
	creditAcc.giveCredit(amount)
	debitAcc.giveDebit(amount)
	
#user input transaction
def userTransaction():
	cAccNum = input("Credit Account Number: ")
	dAccNum = input("Debit Account Number: ")
	amount = input("Amount: ")
	
	try:
		cAcc = eval("a"+cAccNum)
		#isinstance(cAcc, FinancialAccount)
	except NameError:
		print(cAccNum + " doesn't exist")
		return
	
		
	try:
		dAcc = eval("a"+dAccNum)
		#isinstance(dAcc, FinancialAccount)
	except NameError:
		print(dAccNum + " doesn't exist")
		return
		
	cAcc.giveCredit(int(amount))	
	dAcc.giveDebit(int(amount))
	
def foo():
	userTransaction()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
