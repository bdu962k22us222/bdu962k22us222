class Bank_Account:
  def __init__(self):
    self.__name=str(input("enter the name of account holder:"))
    self.__ano=(input("enter the type of account number:"))
    self.__balance=0
    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  def deposit(self):
   self.__amount=float(input("Enter amount to be Deposited:"))
   if self.__amount>0:
      self.__balance+=self.__amount
      print("\n Amount Deposited:", self.__amount)
  def withdraw(self):
   self.__amount=float(input("Enter amount to be withdrawn:"))
   if self.__balance>=self.__amount:
    self.__balance-=self.__amount
    print("\n You withdrew:",self.__amount)
    print("\n Balance:",self.__balance)
   else:
    print("\n Insufficient balance ")
  def display(self):
    print("\n Accountholder name:",self.__name)
    print("\n Account Number:",self.__ano)
    print("\n Net Available Balance=",self.__balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()