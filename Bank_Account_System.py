class Bank_Account_System:

    def __init__(self,username,account_number):

        self.username=username

        self.account_number=account_number

        self.balance=0.0

    def deposit(self,amount):

        self.balance+=amount

    def show_balance(self):

        return f"Current Balance: ₹{self.balance:.2f}"

    def withdraw(self,amount):

        if amount> self.balance:

            return "Insufficient Balance"

        elif amount <=0:

            return "Amount must be greaterthan 0"

        else:

            self.balance-=amount

    def account_details(self):

        return (f"Account Holder: {self.username}\n"f"Account Number: {self.account_number}\n"f"{self.show_balance()}")
 
if __name__ == "__main__":

    username = input("Enter account holder name: ")

    account_number = input("Enter account number: ")
 
    account1 = Bank_Account_System(username, account_number)

    ###account1 = Bank_Account_System("Sukitha", "1234567890")
 
    print(account1.account_details())   

    print(account1.deposit(10000))       

    print(account1.withdraw(1500))      

    print(account1.show_balance())     
 