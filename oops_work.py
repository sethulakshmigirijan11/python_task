
class Bank:
     def __init__(self,name,email,balance):
          self.name=name
          self.email=email
          self.balance=balance
     def initial_balance(self):
          print("Your initial balance :",self.balance)
     def deposit(self,amount):
          if amount<0:
               print("invalid amount")
          if amount>0:
                self.balance+=amount
          print("Amount deposited successfully,your current balance :",self.balance)
     def withdraw(self,amount):
          if amount<0:
               print ("invalid amount")
          if amount>0<self.balance:
                self.balance-=amount
                print("Amount withdraw successfully,your current balance :",self.balance)
     def display_balance(self):
          print("Current balance is :",self.balance)
     def display_details(self):
          print("name :",self.name)
          print("email :",self.email)
          print("balance :",self.balance)

holder=Bank("Sethu","sethu@gmail.com",5000)
holder.display_details()
holder.initial_balance()
holder.deposit(2000)
holder.withdraw(1000)
holder.display_balance()
