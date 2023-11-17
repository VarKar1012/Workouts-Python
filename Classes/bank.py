import datetime

class BankAccount:
    def __init__(self, name, amount, acc_no, date_of_opening) -> None:
        self.name = name
        self.accNo = acc_no
        self.currBalance = amount
        self.openedDate = date_of_opening

    def depositMoney(self, amt):
        self.currBalance += amt
        print(f"The amount {amt} has been deposited in your account.")

    def withdrawMoney(self, amt):
        if amt > self.currBalance:
            print("insufficient balance")
        else:
            self.currBalance -= amt
            print(f"The amount {amt} has been withdrawn from your account.")

    def checkBalance(self):
        print(f"current balance of {self.name} is {self.currBalance}")

    def displayCustomerInfo(self):
        print(f"Name: {self.name}")
        print(f"Account No: {self.accNo}")
        print(f"Date of Joining: {self.openedDate}")
        print(f"Current Balance: {self.currBalance}")

cust1 = BankAccount('varna', 34000, '23433', datetime.date.today())
cust2 = BankAccount('hari', 56000, '56685', '3-2-2020')

cust1.depositMoney(20000)
cust2.depositMoney(10000)

cust1.displayCustomerInfo()
cust2.displayCustomerInfo()

cust1.withdrawMoney(10000)
cust2.withdrawMoney(10000)

cust1.checkBalance()
cust2.checkBalance()
