class Category:
  ledger_list=[]
  def __init__(self,name):
        self.name = name
        self.ledger = []
    
  def deposit(self,amount,description=""):
    self.ledger.append({"amount":amount,"description":description})
    
  def withdraw(self,amount,price):
    if (self.checkfunds(amount)):
      self.ledger.append({"amount":-amount,"description":description})
      return true
    return false
  def get_balance(self):
    total=0
    for item in self.ledger:
      total=total+ item["amount"]
    return total
    





def create_spend_chart(categories):
