#creating a new class and initialising variables
class BankAccount:
  def __init__ (self, account_number, account_holder_name, balance):
    self.account_number = account_number
    self.account_holder_name = account_holder_name
    self.balance = balance
#adding deposits
  def deposit (self, amount):
    self.balance += amount
#subtracting wihdrawals
  def withdraw (self, amount):
    self.balance -= amount
#checking balance
  def get_balance (self):
    return self.balance
#putting the strings to print in the right order
  def display_account_details (self):
    print ("Account Number: " + self.account_number)
    print ("Account Holder Name: " + self.account_holder_name)
    print ("Balance: " + str(self.balance))

#test case
my_account = BankAccount("123456", "John Smith", 500)
my_account.display_account_details()
my_account.deposit(100.00)
my_account.withdraw(50.00)
print(my_account.get_balance())
